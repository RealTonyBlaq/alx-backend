import { createQueue } from "kue";

const queue = createQueue();

const createJob = (phoneNumber, message) => {
  const job = queue.create('push_notification_code', { phoneNumber, message})
    .save((err) => {
      if (err) console.log('Error occured:', err);
      else console.log('Job created:', job.id);
    });
}

createJob('08136882297', 'Money is coming to you');
setTimeout(() => {
  createJob('08033682520', 'Call Mom');
}, 4000);
