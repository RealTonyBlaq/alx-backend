function createPushNotificationsJobs(jobs, queue) {
  if (Array.isArray(jobs)) {
    jobs.forEach((value) => {
      const job = queue.create('push_notification_code_3', value)
        .save((err) => {
          if (err) console.log(`Notification job ${job.id} failed: ${err}`);
          else console.log(`Notification job created: ${job.id}`);
        });

      job.on('failed', (err) => {
        console.log(`Notification job ${job.id} failed: ${err}`);
      });

      job.on('progress', (percent) => {
        console.log(`Notification job ${job.id} ${percent}% complete`);
      });
    
      job.on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
      });
    });
  } else {
    throw new Error('Jobs is not an array');
  }
}
