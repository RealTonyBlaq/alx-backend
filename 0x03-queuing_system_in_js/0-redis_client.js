import { createClient } from "redis";

const client = await createClient();

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
client.on('connection', (stream) => console.log(''))
