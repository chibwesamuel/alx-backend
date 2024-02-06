import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '1234567890',
  message: 'This is a notification message',
};

const job = queue.create('push_notification_code', jobData).save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  } else {
    console.error('Failed to create job:', err);
  }
});

queue.on('job complete', (id) => {
  kue.Job.get(id, (err, job) => {
    if (err) {
      console.error('Failed to get job:', err);
      return;
    }
    console.log('Notification job completed');
    job.remove((removeErr) => {
      if (removeErr) {
        console.error('Failed to remove job:', removeErr);
        return;
      }
      console.log('Job removed');
    });
  });
});

queue.on('job failed', (id) => {
  console.error(`Notification job ${id} failed`);
});

