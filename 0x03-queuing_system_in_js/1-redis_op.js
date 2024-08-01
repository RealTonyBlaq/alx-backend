import { createClient } from "redis";

const client = createClient();

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
    
client.on('ready', () => console.log('Redis client connected to the server'));

await client.connect();

const setNewSchool = (schoolName,)

await client.disconnect();
