import { createClient } from "redis";

async function redisOperations() {
  const client = createClient();

  client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
  client.on('ready', () => console.log('Redis client connected to the server'));

  await client.connect();

  const values = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2
  }

  Object.keys(values).forEach(async (key) => {
    try {
      const reply = await client.hSet('HolbertonSchools', key, values[key]);
      console.log(reply);
    } catch (err) {
      console.log(err);
    }
  });

  try {
    const value = await client.hGetAll('HolbertonSchools');
    console.log(value);
  } catch (err) {
    console.log(err);
  }

  client.quit();
}

redisOperations();
