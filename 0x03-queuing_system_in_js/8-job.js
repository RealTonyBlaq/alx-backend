import { createQueue } from "kue";

function createPushNotificationsJobs(jobs, queue) {
  if (Array.isArray(jobs)) {
    jobs.forEach((value) => {
      queue.create()
    });
  } else {
    throw new Error('Jobs is not an array');
  }
}
