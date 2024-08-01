import { createClient } from "redis";

const client = createClient();

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
client.on('ready', () => console.log('Redis client connected to the server'));

await client.connect();

const publishMessage = (message, time) => {
  setTimeout(async () => {
    console.log(`About to send ${message}`);
    await client.publish('holberton school channel', message);
  }, time);
}

await publishMessage("Holberton Student #1 starts course", 100);
await publishMessage("Holberton Student #2 starts course", 200);
await publishMessage("KILL_SERVER", 300);
await publishMessage("Holberton Student #3 starts course", 400);
