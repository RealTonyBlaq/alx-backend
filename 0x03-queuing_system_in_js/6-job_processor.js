import { createQueue } from "kue";

const job = createQueue('push_notification_code');


const sendNotification = (phoneNumber, message) => {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}
