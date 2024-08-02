import createPushNotificationsJobs from "./8-job";
import { expect } from "chai";
import { createQueue } from "kue";


describe('Testing createPushNotificationJobs', () => {
  beforeEach(() => {
    const queue = createQueue();
    queue.testMode.enter();
  });

  afterEach(() => )
  it('testing jobs created', () => {
    expect(createPushNotificationsJobs).to.be.call
  });
});
