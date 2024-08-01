import { createClient } from "redis";
import { promisify } from 'util';

async function redisOperations() {
  const client = createClient();

  client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
  client.on('ready', () => console.log('Redis client connected to the server'));

  await client.connect();

  const display = promisify(client.get).bind(client);

  const setNewSchool = (schoolName, value) => {
    try {
      const reply = client.set(schoolName, value);
      return reply;
    } catch (err) {
      console.error(err);
      throw err;
    }
  }

  const displaySchoolValue = async (schoolName) => {
    try {
      const value = client.get(schoolName);
      return value;
    } catch (err) {
      console.error(err);
      throw err;
    }
  }

  /* Tests */
  console.log(await displaySchoolValue('Holberton'));
  console.log('Reply:', await setNewSchool('HolbertonSanFrancisco', '100'));
  console.log(await displaySchoolValue('HolbertonSanFrancisco'));
  client.quit();
}

redisOperations();
