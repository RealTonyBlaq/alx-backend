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
    que
  });
  it('testing jobs created', () => {
    expect(createPushNotificationsJobs).to.be.call
  });
});
