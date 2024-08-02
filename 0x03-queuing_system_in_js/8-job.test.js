import createPushNotificationsJobs from "./8-job.js";
import { expect } from "chai";
import { createQueue } from "kue";


describe('Testing createPushNotificationJobs', () => {
  const queue = createQueue();
  beforeEach(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('testing jobs creation error', () => {
    expect(() => createPushNotificationsJobs('Not an array', queue)).to.throw('Jobs is not an array');
    });

  it('testing the created jobs', () => {
    const jobs = [
      {
        phoneNumber: '41535187810',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '41535187810',
        message: 'This is the code 4562 to verify your account'
      },
      {
        phoneNumber: '4153518743',
        message: 'This is the code 4321 to verify your account'
      },
      {
        phoneNumber: '4153538781',
        message: 'This is the code 4562 to verify your account'
      }
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(4);
    jobs.forEach((job, index) => {
      expect(queue.testMode.jobs[index].data).to.deep.equal(job);
      expect(queue.testMode.jobs[index].type).to.equal('push_notification_code_3');
    });
  });
});
