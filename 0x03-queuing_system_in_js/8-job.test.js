import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  before(() => {
    // Set up the Kue queue in test mode
    queue = kue.createQueue({ redis: { host: '127.0.0.1', port: 6379 } });
    queue.testMode.enter();
  });

  after(() => {
    // Clear the queue and exit test mode
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs({}, queue)).to.throw('Jobs is not an array');
  });

  it('should create two new jobs to the queue', () => {
    const jobs = [
      { phoneNumber: '123', message: 'Test message 1' },
      { phoneNumber: '456', message: 'Test message 2' }
    ];
    createPushNotificationsJobs(jobs, queue);
    console.log('Jobs in the queue:', queue.testMode.jobs);
    expect(queue.testMode.jobs.length).to.equal(2);
  });
});
