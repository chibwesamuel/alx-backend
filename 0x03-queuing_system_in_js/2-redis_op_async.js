import redis from 'redis';
import { promisify } from 'util';

// Create a Redis client
const client = redis.createClient();

// Promisify Redis functions
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Event listener for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event listener for connection errors
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

// Function to set a new school value in Redis
async function setNewSchool(schoolName, value) {
  try {
    const reply = await setAsync(schoolName, value);
    console.log(`Value set for ${schoolName}: ${value}`);
    console.log('Reply:', reply);
  } catch (err) {
    console.error(`Error setting value in Redis: ${err}`);
  }
}

// Function to display the value of a school in Redis using async/await
async function displaySchoolValue(schoolName) {
  try {
    const reply = await getAsync(schoolName);
    console.log(`Value for ${schoolName}: ${reply}`);
  } catch (err) {
    console.error(`Error getting value from Redis: ${err}`);
  }
}

// Call the functions
(async () => {
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
