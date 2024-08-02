import createPushNotificationsJobs from "./8-job";
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
    expect(createPushNotificationsJobs('Not an array', queue)).to.throw('Jobs is not an array');
  });

  it('testing the created jobs', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      },
      
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);
  });
});
