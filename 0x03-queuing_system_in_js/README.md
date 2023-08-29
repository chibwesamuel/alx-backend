## Queuing System in JS

In this project, I have developed a queuing system using Node.js and Redis. The queuing system involves creating, processing, and tracking jobs in a background worker setup. The primary components of this project include:

### Task 0: Installing a Redis Instance

In this task, I installed a Redis instance and performed various operations using the Redis server and client. This included starting the Redis server, setting and getting values from Redis, and working with the Redis client.

### Task 1: Node Redis Client

In this task, I wrote a Node.js script named `0-redis_client.js` to connect to the Redis server. The script logs messages based on successful and unsuccessful connections to the Redis server.

### Task 2: Node Redis Client and Basic Operations

In this task, I extended the Redis client script to perform basic operations such as setting new values in Redis and displaying the values for specific keys. The script `1-redis_op.js` contains functions to set new school values and display school values based on keys.

### Task 3: Node Redis Client and Async Operations

In this task, I continued to work with the Redis client script and used the `promisify` function to enable asynchronous operations. The script `2-redis_op_async.js` demonstrates the usage of `async/await` with Redis operations.

### Task 4: Node Redis Client and Advanced Operations

This task involved using the Redis client to work with hash values. I created a hash with multiple key-value pairs and demonstrated operations like setting and displaying hash values. The script `4-redis_advanced_op.js` contains these advanced Redis operations.

### Task 5: Node Redis Client Publisher and Subscriber

Here, I implemented a Redis publisher and subscriber system. Two scripts, `5-publisher.js` and `5-subscriber.js`, were created to showcase sending and receiving messages through Redis channels.

### Task 6: Create the Job Creator

In this task, I implemented a job creation system using Kue, a Redis-based priority job queue. The script `6-job_creator.js` creates and logs jobs to be processed.

### Task 7: Create the Job Processor

Task 7 involved building a job processing module. The script `6-job_processor.js` processes jobs created in the previous task using Kue's queue processing capabilities.

### Task 8: Writing the Job Creation Function

In this task, I created a function to create multiple jobs using Kue. The script `8-job.js` includes the function to create and manage job creation.

### Task 9: Writing the Test for Job Creation

I created test cases for the job creation function using Mocha. The script `8-job.test.js` contains the test suite for the job creation process.

### Task 10: In Stock?

This task focused on creating a web application to manage product stocks using Express and Redis. The application provides routes to list products, display product details, and reserve products based on availability. The script `9-stock.js` contains the implementation of this system.

### Task 13: Can I Have a Seat?

In this advanced task, I built a system to manage seat reservations using Express, Redis, and Kue. The application allows users to check available seats and reserve seats if they are available. The script `100-seat.js` implements this seat reservation system.

This project showcases various aspects of working with Redis, job queues, asynchronous operations, and web applications in Node.js. Each task builds upon the previous one to create a comprehensive queuing system.
