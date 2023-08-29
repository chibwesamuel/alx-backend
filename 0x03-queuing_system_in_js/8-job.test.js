import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job';

describe('createPushNotificationsJobs', function () {
  let queue;

  before(function () {
    // Create a Kue queue in test mode
    queue = kue.createQueue({ testMode: true });
  });

  after(function () {
    // Clear the queue and exit test mode
    queue.clear();
    queue.testMode.exit();
  });

  it('should throw an error if jobs is not an array', function () {
    expect(() => createPushNotificationsJobs({}, queue)).to.throw('Jobs is not an array');
  });

  it('should create new jobs in the queue', function () {
    const jobs = [
      { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
      { phoneNumber: '4153518781', message: 'This is the code 5678 to verify your account' },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
    // Add more assertions as needed
  });
  
  // Add more test cases as needed
});
