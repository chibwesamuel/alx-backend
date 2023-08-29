import express from 'express';
import redis from 'redis';
import kue from 'kue';
import { promisify } from 'util';

const app = express();
const port = 1245;

// Create Redis client
const redisClient = redis.createClient();
const setAsync = promisify(redisClient.set).bind(redisClient);
const getAsync = promisify(redisClient.get).bind(redisClient);

// Reserve a seat
function reserveSeat(number) {
  return setAsync('available_seats', number);
}

// Get current available seats
async function getCurrentAvailableSeats() {
  const seats = await getAsync('available_seats');
  return parseInt(seats, 10) || 0;
}

// Initialize available seats to 50
reserveSeat(50);

// Initialize reservationEnabled
let reservationEnabled = true;

// Create Kue queue
const queue = kue.createQueue();

// Middleware to parse JSON
app.use(express.json());

// Route to get number of available seats
app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats });
});

// Route to reserve a seat
app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
    return;
  }

  const job = queue.create('reserve_seat').save(err => {
    if (err) {
      res.json({ status: 'Reservation failed' });
    } else {
      res.json({ status: 'Reservation in process' });
    }
  });
});

// Route to process the queue
app.get('/process', (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    const currentSeats = await getCurrentAvailableSeats();
    if (currentSeats === 0) {
      reservationEnabled = false;
    }

    if (currentSeats >= 0) {
      reserveSeat(currentSeats - 1);
      done();
    } else {
      done(new Error('Not enough seats available'));
    }
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
