import { createClient } from "redis";

async function test_connection() {
    const client = createClient();

    client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
    
    await client.connect()
    
    client.on('connected', (stream) => console.log('Redis client connected to the server'));
    
    await client.disconnect();
}

test_connection();
