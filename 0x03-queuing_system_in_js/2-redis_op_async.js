import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  const reply = await getAsync(schoolName);
  console.log(reply);
}

(async () => {
  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');
})();
