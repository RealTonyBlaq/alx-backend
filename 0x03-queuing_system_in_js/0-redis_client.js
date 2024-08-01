import { createClient } from "redis";

async function test_connection() {
    const client = createClient();

    client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
    
    client.on('ready', (stream) => console.log('Redis client connected to the server'));

    await client.connect();
    await client.disconnect();
}

test_connection();
