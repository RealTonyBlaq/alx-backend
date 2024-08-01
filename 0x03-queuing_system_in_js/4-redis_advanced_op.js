import { createClient } from "redis";
import { promisify } from 'util';

async function redisOperations() {
  const client = createClient();

  client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
  client.on('ready', () => console.log('Redis client connected to the server'));

  await client.connect();

  client.hSet('')

  client.quit();
}
