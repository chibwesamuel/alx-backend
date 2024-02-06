import express from 'express';
import redis from 'redis';
import kue from 'kue';
import { promisify } from 'util';

const app = express();
const port = 1245;

// Redis client
const redisClient = redis.createClient();
const getAsync = promisify(redisClient.get).bind(redisClient);
const setAsync = promisify(redisClient.set).bind(redisClient);

// Reserve seat function
const reserveSeat = async (number) => {
  await setAsync('available_seats', number);
};

// Get current available seats function
const getCurrentAvailableSeats = async () => {
  const availableSeats = await getAsync('available_seats');
  return availableSeats ? parseInt(availableSeats) : 0;
};

// Initialize available seats to 50
reserveSeat(50);

// Initialize reservationEnabled to true
let reservationEnabled = true;

// Kue queue
const queue = kue.createQueue();

// Route to get available seats
app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: numberOfAvailableSeats });
});

// Route to reserve a seat
app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
    return;
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (!err) {
      res.json({ status: 'Reservation in process' });
    } else {
      res.json({ status: 'Reservation failed' });
    }
  });

  job.on('complete', (result) => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });
});

// Route to process the queue
app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  const currentAvailableSeats = await getCurrentAvailableSeats();
  if (currentAvailableSeats > 0) {
    await reserveSeat(currentAvailableSeats - 1);
    if (currentAvailableSeats - 1 === 0) {
      reservationEnabled = false;
    }
  } else {
    queue.shutdown(5000, () => {
      console.log('Queue shutdown');
    });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});

