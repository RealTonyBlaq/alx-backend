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
    expect(createPushNotificationsJobs('Not an array')).to.throw('Jobs is not an array')
  });
});
