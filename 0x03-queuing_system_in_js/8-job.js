import { createQueue } from "kue";

function createPushNotificationsJobs(jobs, queue) {
  if (Array.isArray(jobs)) {
    jobs.forEach((value) => {
      const job = queue.create('push_notification_code_3', value)
        .save((err) => {
          if (err) console.log(`Notification job ${job.id} failed: ${err}`);
          else console.log(`Notification job created: ${job.id}`);
        });
        
    });
  } else {
    throw new Error('Jobs is not an array');
  }
}
