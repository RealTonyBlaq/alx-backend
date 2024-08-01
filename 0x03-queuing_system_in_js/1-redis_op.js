import { createClient } from "redis";

const client = createClient();

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
client.on('ready', () => console.log('Redis client connected to the server'));

await client.connect();

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, (err, reply) => {
    if (err) console.error(err);
    else console.log(reply);
  });
}

const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (err, value) => {
    if (err) console.error(err);
    else console.log(value);
  });
}

/* Tests  */
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

await client.disconnect();
