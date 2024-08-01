import { createClient } from "redis";

const client = await createClient();

client.on('error', (err) => console.log('Redis client connected to the server'));
client.on('connection')
