import { createQueue } from "kue";

const queue = createQueue();

const blackListedNumbers = [4153518780, 4153518781];

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);

  if (blackListedNumbers.includes())
}
