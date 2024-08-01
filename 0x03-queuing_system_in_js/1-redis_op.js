import { createClient } from "redis";
import print from "redis";

const client = createClient();

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
    
client.on('ready', () => console.log('Redis client connected to the server'));

await client.connect();

const setNewSchool = async (schoolName, value) => {
  await client.set(schoolName, value, print);
  
}

const displaySchoolValue = async (schoolName) => {
  await client.get(schoolName, (value) => console.log(value));
}

/* Tests */
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

await client.disconnect();
