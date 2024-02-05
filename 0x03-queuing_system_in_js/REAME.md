# Queuing System in JS

This repository contains a set of tasks focusing on implementing a queuing system in JavaScript using Redis. Below I give a summary of the tasks and their requirements:

## Tasks

### 0. Install a Redis Instance
- Download, extract, and compile the latest stable Redis version.
- Start Redis in the background and ensure it's working correctly.
- Copy the Redis dump file into the project root.

### 1. Node Redis Client
- Install `node_redis` using npm.
- Write a script to connect to the Redis server and handle connection errors.

### 2. Node Redis Client and Basic Operations
- Implement basic Redis operations like setting and retrieving values.
- Use callbacks for operations.

### 3. Node Redis Client and Async Operations
- Use `promisify` to handle asynchronous operations.
- Achieve the same results as Task 2.

### 4. Node Redis Client and Advanced Operations
- Store hash values in Redis.
- Use callbacks for operations.

### 5. Node Redis Client Publisher and Subscriber
- Implement a publisher and subscriber model using Redis.
- Handle connection and message events.

### 6. Create the Job Creator
- Implement a job creator using Kue.
- Create and manage job objects.

### 7. Create the Job Processor
- Implement a job processor using Kue.
- Process jobs and handle completion, failure, and progress.

### 8. Track Progress and Errors with Kue: Create the Job Creator
- Create jobs and track their progress and errors.
- Use Kue to set up the queue.

### 9. Track Progress and Errors with Kue: Create the Job Processor
- Implement a job processor that tracks progress and handles errors.
- Use Kue to set up the queue.

### 10. Writing the Job Creation Function
- Write a function to create jobs and manage them in the queue.
- Log job status and progress.

### 11. Writing the Test for Job Creation
- Write tests for the job creation function.
- Use queue.testMode to validate jobs.

### 12. In Stock?
- Create a server and data access functions.
- Provide routes to list available products.

### 13. Can I Have a Seat? (Advanced)
- Create a Redis client and Kue queue.
- Implement seat reservation functionality with error handling.

These tasks cover various aspects of implementing a queuing system in JavaScript using Redis and Kue. Each task has specific requirements and implementations aimed at achieving the desired functionality.