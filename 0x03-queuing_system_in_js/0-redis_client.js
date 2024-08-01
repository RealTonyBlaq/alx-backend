import { createClient } from "redis";

const client = await createClient();

client.on('error', (err) => });
