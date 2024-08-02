import { createQueue } from "kue";

function createPushNotificationsJobs(jobs, queue) {
  if (Array.isArray(jobs)) {
    jobs.forEach((value) => {
      queue.create('push_notification_code_3', ())
    });
  } else {
    throw new Error('Jobs is not an array');
  }
}
