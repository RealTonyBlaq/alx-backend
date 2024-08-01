import { createClient } from "redis";
import redis from "redis";

const client = createClient();
const print = redis.print

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
    
client.on('ready', () => console.log('Redis client connected to the server'));

await client.connect();

const setNewSchool = async (schoolName, value) => {
  await client.set(schoolName, value, print);
}

const displaySchoolValue = async (schoolName) => {
  await client.get(schoolName, (err, value) => {
    if (err) console.log(err);
    else console.log(value);
  });
}

/* Tests */
await displaySchoolValue('Holberton');
await setNewSchool('HolbertonSanFrancisco', '100');
await displaySchoolValue('HolbertonSanFrancisco');

await client.disconnect();
