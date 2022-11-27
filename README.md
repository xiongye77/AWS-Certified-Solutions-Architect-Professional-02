# AWS-Certified-Solutions-Architect-Professional-02

Amazon SNS message deliveries to AWS Lambda have crossed the account concurrency quota for Lambda, so the team needs to contact AWS support to raise the account limit
Amazon Simple Notification Service (SNS) is a highly available, durable, secure, fully managed pub/sub messaging service that enables you to decouple microservices, distributed systems, and serverless applications.
AWS Lambda currently supports 1000 concurrent executions per AWS account per region. If your Amazon SNS message deliveries to AWS Lambda contribute to crossing these concurrency quotas, your Amazon SNS message deliveries will be throttled. You need to contact AWS support to raise the account limit.
![image](https://user-images.githubusercontent.com/36766101/204115857-d0d17f06-2889-4fad-b47d-5fee86c1e5e6.png)




AWS DataSync is an online data transfer service that simplifies, automates, and accelerates copying large amounts of data to and from AWS storage services over the internet or AWS Direct Connect.
AWS DataSync fully automates and accelerates moving large active datasets to AWS, up to 10 times faster than command-line tools. It is natively integrated with Amazon S3, Amazon EFS, Amazon FSx for Windows File Server, Amazon CloudWatch, and AWS CloudTrail, which provides seamless and secure access to your storage services, as well as detailed monitoring of the transfer.
DataSync uses a purpose-built network protocol and scale-out architecture to transfer data. A single DataSync agent is capable of saturating a 10 Gbps network link. DataSync fully automates the data transfer. It comes with retry and network resiliency mechanisms, network optimizations, built-in task scheduling, monitoring via the DataSync API and Console, and CloudWatch metrics, events, and logs that provide granular visibility into the transfer process. DataSync performs data integrity verification both during the transfer and at the end of the transfer.
![image](https://user-images.githubusercontent.com/36766101/204115843-6ef38b3a-5005-4f22-bdd0-0f8e7175adf7.png)



AWS Lambda lets you run code without provisioning or managing servers. You pay only for the compute time you consume. Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. SQS offers two types of message queues. Standard queues offer maximum throughput, best-effort ordering, and at-least-once delivery. SQS FIFO queues are designed to guarantee that messages are processed exactly once, in the exact order that they are sent.
You can use an AWS Lambda function to process messages in an Amazon Simple Queue Service (Amazon SQS) queue. Lambda event source mappings support standard queues and first-in, first-out (FIFO) queues. With Amazon SQS, you can offload tasks from one component of your application by sending them to a queue and processing them asynchronously.


A VPC endpoint enables you to privately connect your VPC to supported AWS services and VPC endpoint services powered by AWS PrivateLink without requiring an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. Instances in your VPC do not require public IP addresses to communicate with resources in the service. Traffic between your VPC and the other service does not leave the Amazon network.
A gateway endpoint is a gateway that you specify as a target for a route in your route table for traffic destined to a supported AWS service. One of the ways of letting EC2 instances running in private subnets of a VPC access S3 based resources is by setting up NAT instances in a public subnet and then access those S3 based resources. However, there is a more efficient and secure way. The EC2 instances running in private subnets of a VPC can control access to S3 buckets, objects, and API functions that are in the same Region as the VPC by using the S3 gateway endpoints.

You can further use an S3 bucket policy to indicate which VPCs and which VPC Endpoints have access to your S3 buckets.
![image](https://user-images.githubusercontent.com/36766101/204116046-d66939fd-35b0-4c93-8d70-6a7a3eaeef3d.png)



Amazon Kinesis Data Firehose is the easiest way to reliably load streaming data into data lakes, data stores, and analytics tools. It is a fully managed service that automatically scales to match the throughput of your data and requires no ongoing administration. It can also batch, compress, transform, and encrypt the data before loading it, minimizing the amount of storage used at the destination and increasing security.
When a Kinesis data stream is configured as the source of a Firehose delivery stream, Firehose’s PutRecord and PutRecordBatch operations are disabled and Kinesis Agent cannot write to Firehose delivery stream directly. Data needs to be added to the Kinesis data stream through the Kinesis Data Streams PutRecord and PutRecords operations instead. Therefore, this option is correct.
![image](https://user-images.githubusercontent.com/36766101/204116205-7c8952a0-1af8-4b93-abcc-f453d9c60502.png)


Process and analyze the Amazon CloudWatch Logs for Lambda function to determine processing times for requested images at pre-configured intervals
To help you troubleshoot failures in a function, the Lambda service logs all requests handled by a Lambda function and also automatically stores logs generated by your code through Amazon CloudWatch Logs. You can insert logging statements into your code to determine processing times for requested images. These logs can then be processed at certain pre-configured intervals for further analysis.

Process and analyze the AWS X-Ray traces and analyze HTTP methods to determine the root cause of the HTTP errors
You can use AWS X-Ray to visualize the components of your application, identify performance bottlenecks such as the one described in the use-case for processing images and troubleshoot those requests that resulted in an error. Your Lambda functions send trace data to X-Ray, and X-Ray processes the data to generate a service map and searchable trace summaries.
