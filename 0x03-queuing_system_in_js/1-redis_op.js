import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Event listener for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event listener for connection errors
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

// Function to set a new school value in Redis
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.error(`Error setting value in Redis: ${err}`);
    } else {
      console.log(`Value set for ${schoolName}: ${value}`);
      console.log(reply); // redis.print is not available, so logging the reply instead
    }
  });
}

// Function to display the value of a school in Redis
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(`Error getting value from Redis: ${err}`);
    } else {
      console.log(`Value for ${schoolName}: ${reply}`);
    }
  });
}

// Call the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
