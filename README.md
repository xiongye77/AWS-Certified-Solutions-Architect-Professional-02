# AWS-Certified-Solutions-Architect-Professional-02


![image](https://user-images.githubusercontent.com/36766101/204118816-da3ef40b-633b-4a31-aed0-79b2e052e0ad.png)

Amazon SNS message deliveries to AWS Lambda have crossed the account concurrency quota for Lambda, so the team needs to contact AWS support to raise the account limit
Amazon Simple Notification Service (SNS) is a highly available, durable, secure, fully managed pub/sub messaging service that enables you to decouple microservices, distributed systems, and serverless applications.
AWS Lambda currently supports 1000 concurrent executions per AWS account per region. If your Amazon SNS message deliveries to AWS Lambda contribute to crossing these concurrency quotas, your Amazon SNS message deliveries will be throttled. You need to contact AWS support to raise the account limit.
![image](https://user-images.githubusercontent.com/36766101/204115857-d0d17f06-2889-4fad-b47d-5fee86c1e5e6.png)



![image](https://user-images.githubusercontent.com/36766101/204118709-cf8abdee-d158-4d2f-b118-d590e72d82c3.png)

AWS DataSync is an online data transfer service that simplifies, automates, and accelerates copying large amounts of data to and from AWS storage services over the internet or AWS Direct Connect.
AWS DataSync fully automates and accelerates moving large active datasets to AWS, up to 10 times faster than command-line tools. It is natively integrated with Amazon S3, Amazon EFS, Amazon FSx for Windows File Server, Amazon CloudWatch, and AWS CloudTrail, which provides seamless and secure access to your storage services, as well as detailed monitoring of the transfer.
DataSync uses a purpose-built network protocol and scale-out architecture to transfer data. A single DataSync agent is capable of saturating a 10 Gbps network link. DataSync fully automates the data transfer. It comes with retry and network resiliency mechanisms, network optimizations, built-in task scheduling, monitoring via the DataSync API and Console, and CloudWatch metrics, events, and logs that provide granular visibility into the transfer process. DataSync performs data integrity verification both during the transfer and at the end of the transfer.
![image](https://user-images.githubusercontent.com/36766101/204115843-6ef38b3a-5005-4f22-bdd0-0f8e7175adf7.png)


![image](https://user-images.githubusercontent.com/36766101/204118702-5c50534d-0c67-4df9-9bb8-bcf42f7622c6.png)

AWS Lambda lets you run code without provisioning or managing servers. You pay only for the compute time you consume. Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. SQS offers two types of message queues. Standard queues offer maximum throughput, best-effort ordering, and at-least-once delivery. SQS FIFO queues are designed to guarantee that messages are processed exactly once, in the exact order that they are sent.
You can use an AWS Lambda function to process messages in an Amazon Simple Queue Service (Amazon SQS) queue. Lambda event source mappings support standard queues and first-in, first-out (FIFO) queues. With Amazon SQS, you can offload tasks from one component of your application by sending them to a queue and processing them asynchronously.

![image](https://user-images.githubusercontent.com/36766101/204118720-ddde2015-5d6b-4ad3-88e2-505e12dcddc6.png)

A VPC endpoint enables you to privately connect your VPC to supported AWS services and VPC endpoint services powered by AWS PrivateLink without requiring an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. Instances in your VPC do not require public IP addresses to communicate with resources in the service. Traffic between your VPC and the other service does not leave the Amazon network.
A gateway endpoint is a gateway that you specify as a target for a route in your route table for traffic destined to a supported AWS service. One of the ways of letting EC2 instances running in private subnets of a VPC access S3 based resources is by setting up NAT instances in a public subnet and then access those S3 based resources. However, there is a more efficient and secure way. The EC2 instances running in private subnets of a VPC can control access to S3 buckets, objects, and API functions that are in the same Region as the VPC by using the S3 gateway endpoints.

You can further use an S3 bucket policy to indicate which VPCs and which VPC Endpoints have access to your S3 buckets.
![image](https://user-images.githubusercontent.com/36766101/204116046-d66939fd-35b0-4c93-8d70-6a7a3eaeef3d.png)


![image](https://user-images.githubusercontent.com/36766101/204118846-16ce4011-6c9e-4268-8d71-8e3959080491.png)

Amazon Kinesis Data Firehose is the easiest way to reliably load streaming data into data lakes, data stores, and analytics tools. It is a fully managed service that automatically scales to match the throughput of your data and requires no ongoing administration. It can also batch, compress, transform, and encrypt the data before loading it, minimizing the amount of storage used at the destination and increasing security.
When a Kinesis data stream is configured as the source of a Firehose delivery stream, Firehose’s PutRecord and PutRecordBatch operations are disabled and Kinesis Agent cannot write to Firehose delivery stream directly. Data needs to be added to the Kinesis data stream through the Kinesis Data Streams PutRecord and PutRecords operations instead. Therefore, this option is correct.
![image](https://user-images.githubusercontent.com/36766101/204116205-7c8952a0-1af8-4b93-abcc-f453d9c60502.png)



![image](https://user-images.githubusercontent.com/36766101/204118730-fdc67b0b-6b33-457e-8f49-b4c2b1cb7c5d.png)

Process and analyze the Amazon CloudWatch Logs for Lambda function to determine processing times for requested images at pre-configured intervals
To help you troubleshoot failures in a function, the Lambda service logs all requests handled by a Lambda function and also automatically stores logs generated by your code through Amazon CloudWatch Logs. You can insert logging statements into your code to determine processing times for requested images. These logs can then be processed at certain pre-configured intervals for further analysis.

Process and analyze the AWS X-Ray traces and analyze HTTP methods to determine the root cause of the HTTP errors
You can use AWS X-Ray to visualize the components of your application, identify performance bottlenecks such as the one described in the use-case for processing images and troubleshoot those requests that resulted in an error. Your Lambda functions send trace data to X-Ray, and X-Ray processes the data to generate a service map and searchable trace summaries.







Set up Systems Manager Agent on all instances to manage patching. Test patches in pre-production and then deploy as a maintenance window task with the appropriate approval
Apply patch baselines using the AWS-RunPatchBaseline SSM document

Systems Manager is an AWS service that you can use to view and control your infrastructure on AWS. Using the Systems Manager console, you can view operational data from multiple AWS services and automate operational tasks across your AWS resources. Systems Manager helps you maintain security and compliance by scanning your managed instances and reporting on (or taking corrective action on) any policy violations it detects. AWS Systems Manager Agent (SSM Agent) is Amazon software that can be installed and configured on an EC2 instance, an on-premises server, or a virtual machine (VM). SSM Agent makes it possible for Systems Manager to update, manage, and configure these resources.

You can use Patch Manager to apply patches for both operating systems and applications. (On Windows Server, application support is limited to updates for Microsoft applications). Patch Manager uses patch baselines, which include rules for auto-approving patches within days of their release, as well as a list of approved and rejected patches. You can install patches individually or to large groups of instances by using Amazon EC2 tags.
For the given use-case, you can install patches on a regular basis by scheduling patching to run as a Systems Manager maintenance window task.
Systems Manager supports an SSM document for Patch Manager, AWS-RunPatchBaseline, which performs patching operations on instances for both security-related and other types of updates. When the document is run, it uses the patch baseline currently specified as the "default" for an operating system type.


![image](https://user-images.githubusercontent.com/36766101/204118742-05c851bc-ddee-4f0d-92a1-01d0b916858d.png)


Configure SAML-based authentication tied to an IAM role that has the PowerUserAccess managed policy attached to it. Attach a customer-managed policy that denies access to RDS in any AWS Region except us-east-1. (PowerUserAccess = AdministrativeAccess - IAM)
![image](https://user-images.githubusercontent.com/36766101/204118505-63ad7539-514a-417c-8544-354ca42e96cf.png)

Security Assertion Markup Language 2.0 (SAML) is an open federation standard that allows an identity provider (IdP) to authenticate users and pass identity and security information about them to a service provider which is an AWS application or service for the current use-case. With SAML, you can enable a single sign-on experience for your users across many SAML-enabled applications and services. Users authenticate with the IdP once using a single set of credentials, and then get access to multiple applications and services without additional sign-ins.

For the given scenario, the company wants to control access to on-premises as well as AWS Cloud resources (specifically via the AWS Management Console) using Active Directory, so it should use SAML 2.0 federated users to access the AWS Management Console. You also create an IAM role with a trust policy that sets the SAML provider as the principal, which establishes a trust relationship between your organization and AWS. The role's permission policy establishes what users from your organization are allowed to do in AWS. In this case, the role will have a PowerUserAccess managed policy attached. As the PowerUserAccess managed policy will allow the developers to create RDS instances in any Region, therefore, you also need to attach a customer-managed policy that denies access to RDS in any AWS Region except us-east-1.


![image](https://user-images.githubusercontent.com/36766101/204118746-622c84c8-2105-43de-a528-3c95c646f89e.png)


Use EFS as the data tier of the storage layer

Amazon Elastic File System (Amazon EFS) provides a simple, scalable, fully managed elastic NFS file system for use with AWS Cloud services and on-premises resources.

Amazon EFS is a Regional service storing data within and across multiple Availability Zones (AZs) for high availability and durability. Amazon EC2 instances can access your file system across AZs, Regions, and VPCs, while on-premises servers can access using AWS Direct Connect or AWS VPN. You can connect to Amazon EFS file systems from EC2 instances in other AWS Regions using an inter-Region VPC peering connection, and from on-premises servers using an AWS VPN connection. EFS is also POSIX compliant and can be shared across many systems, so it fits the given use-case.

Use EC2 Instance Store as the service tier of the storage layer
An instance store (also known as ephemeral storage) provides temporary block-level storage for your instance. This storage is located on disks that are physically attached to the host computer. Instance store is ideal for the temporary storage of information that changes frequently such as buffers, caches, scratch data, and other temporary content, or for data that is replicated across a fleet of instances, such as a load-balanced pool of web servers. Instance store volumes are included as part of the instance's usage cost.

As Instance Store based volumes provide high random I/O performance at low cost (as the storage is part of the instance's usage cost) and the fault-tolerant architecture can adjust for the loss of any instance, therefore you should use Instance Store based EC2 instances for this use-case.


![image](https://user-images.githubusercontent.com/36766101/204118823-ee1cca41-713b-4820-860e-1a57efb7f212.png)


If a user or role has an IAM permission policy that grants access to an action that is either not allowed or explicitly denied by the applicable SCPs, the user or role can't perform that action.
Service control policies (SCPs) are one type of policy that can be used to manage your organization. SCPs offer central control over the maximum available permissions for all accounts in your organization, allowing you to ensure your accounts stay within your organization’s access control guidelines.


SCPs affect all users and roles in attached accounts, including the root user

SCPs do not affect service-linked role




![image](https://user-images.githubusercontent.com/36766101/204159843-3dc2412f-e8f0-4d90-b0d0-c190ae78f74f.png)
AWS Direct Connect is a cloud service solution that makes it easy to establish a dedicated network connection from your premises to AWS. AWS Direct Connect lets you establish a dedicated network connection between your network and one of the AWS Direct Connect locations.

With AWS Direct Connect plus VPN, you can combine one or more AWS Direct Connect dedicated network connections with the Amazon VPC VPN. This combination provides an IPsec-encrypted private connection that also reduces network costs, increases bandwidth throughput, and provides a more consistent network experience than internet-based VPN connections. This solution combines the AWS managed benefits of the VPN solution with low latency, increased bandwidth, more consistent benefits of the AWS Direct Connect solution, and an end-to-end, secure IPsec connection. Therefore, AWS Direct Connect plus VPN is the correct solution for this use-case.



![image](https://user-images.githubusercontent.com/36766101/204159952-fff6c9a0-76b2-44a0-abb8-5750582029d8.png)
The AWS Snowball Edge is a type of Snowball device with on-board storage and compute power for select AWS capabilities. Each Snowball Edge device can transport data at speeds faster than the internet. This transport is done by shipping the data in the appliances through a Regional carrier. The appliances are rugged shipping containers, complete with E Ink shipping labels. Snowball Edge devices have three options for device configurations – storage optimized, compute optimized, and with GPU.

Snowball Edge is the optimal choice if you need to securely and quickly transfer dozens of terabytes to petabytes of data to AWS. The AWS Snow Family is ideal for customers moving large batches of data at once. The AWS Snowball has a typical 5-7 days turnaround time. As each Snowball Edge device can handle 80TB of data, you can order 3 such devices to take care of the data transfer for the given use-case.



![image](https://user-images.githubusercontent.com/36766101/204161023-2cda23dd-9d09-456c-bb81-a5a0ce6b642a.png)

API Gateway creates RESTful APIs that: Are HTTP-based. Enable stateless client-server communication. Implement standard HTTP methods such as GET, POST, PUT, PATCH, and DELETE.
API Gateway creates WebSocket APIs that: Adhere to the WebSocket protocol, which enables stateful, full-duplex communication between client and server. Route incoming messages based on message content.

So API Gateway supports stateless RESTful APIs as well as stateful WebSocket APIs.


![image](https://user-images.githubusercontent.com/36766101/204161368-2b5dfa9d-55ca-481f-aa19-35f24471fea6.png)
Recovery time objective (RTO) and recovery point objective (RPO) are two key metrics to consider when developing a DR plan. RTO represents how many hours it takes you to return to a working state after a disaster.

Automated backups, manual snapshots and Read Replicas are supported across multiple Regions - The automated backup feature of Amazon RDS enables point-in-time recovery for your database instance. Amazon RDS will backup your database and transaction logs and store both for a user-specified retention period. If it’s a Multi-AZ configuration, backups occur on the standby to reduce I/O impact on the primary. Amazon RDS supports Cross-Region Automated Backups. Manual snapshots and Read Replicas are also supported across multiple Regions.

Database snapshots are user-initiated backups of your complete DB instance that serve as full backups. These snapshots can be copied and shared to different Regions and accounts - Database snapshots are manual (user-initiated) backups of your complete DB instance that serve as full backups. They’re stored in Amazon S3 and are retained until you explicitly delete them. These snapshots can be copied and shared to different Regions and accounts. Because DB snapshots include the entire DB instance, including data files and temporary files, the size of the instance affects the amount of time it takes to create the snapshot.


![image](https://user-images.githubusercontent.com/36766101/204162448-ed7f7fba-d646-4476-a56d-a782edabee5b.png)
Create an application that will traverse the S3 bucket, issue a Byte Range Fetch for the first 250 bytes, and store that information in ElasticSearch

Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance.

Amazon Elasticsearch Service (Amazon ES) is a managed service that makes it easy to deploy, operate, and scale Elasticsearch clusters in the AWS Cloud. Elasticsearch is a popular open-source search and analytics engine for use cases such as log analytics, real-time application monitoring, and clickstream analysis. With Amazon ES, you get direct access to the Elasticsearch APIs; existing code and applications work seamlessly with the service.Using the Range HTTP header in a GET Object request, you can fetch a byte-range from an object, transferring only the specified portion. You can use concurrent connections to Amazon S3 to fetch different byte ranges from within the same object. This helps you achieve higher aggregate throughput versus a single whole-object request. Fetching smaller ranges of a large object also allows your application to improve retry times when requests are interrupted.
A byte-range request is a perfect way to get the beginning of a file and ensuring we remain efficient during our scan of our S3 bucket. You can then store the relevant information in the form of a JSON document in ElasticSearch.

Create an application that will use the S3 Select ScanRange parameter to get the first 250 bytes and store that information in ElasticSearch
With Amazon S3 Select, you can scan a subset of an object by specifying a range of bytes to query using the ScanRange parameter. This capability lets you parallelize scanning the whole object by splitting the work into separate Amazon S3 Select requests for a series of non-overlapping scan ranges. Use the Amazon S3 Select ScanRange parameter and Start at (Byte) and End at (Byte). You can then store the relevant information in the form of a JSON document in ElasticSearch.



![image](https://user-images.githubusercontent.com/36766101/204162766-90d35fd2-ed85-41ea-b925-007a45bb4302.png)
By default, an S3 object is owned by the AWS account that uploaded it. So the S3 bucket owner will not implicitly have access to the objects written by Redshift cluster - By default, an S3 object is owned by the AWS account that uploaded it. This is true even when the bucket is owned by another account. Because the Amazon Redshift data files from the UNLOAD command were put into your bucket by another account, you (the bucket owner) don't have default permission to access those files.


![image](https://user-images.githubusercontent.com/36766101/204165464-70a482de-1d54-4d40-81a5-f46c49b45842.png)
Develop the leaderboard using ElastiCache Redis as it meets the in-memory, high availability, low latency requirements
Amazon ElastiCache for Redis is a blazing fast in-memory data store that provides sub-millisecond latency to power internet-scale real-time applications. Amazon ElastiCache for Redis is a great choice for real-time transactional and analytical processing use cases such as caching, chat/messaging, gaming leaderboards, geospatial, machine learning, media streaming, queues, real-time analytics, and session store. ElastiCache for Redis can be used to power the live leaderboard, so this option is correct.

Develop the leaderboard using DynamoDB with DynamoDB Accelerator (DAX) as it meets the in-memory, high availability, low latency requirements
Amazon DynamoDB is a key-value and document database that delivers single-digit millisecond performance at any scale. It's a fully managed, multi-Region, multi-master, durable database with built-in security, backup and restore, and in-memory caching for internet-scale applications.
DAX is a DynamoDB-compatible caching service that enables you to benefit from fast in-memory performance for demanding applications. So DynamoDB with DAX can be used to power the live leaderboard.



![image](https://user-images.githubusercontent.com/36766101/204165595-9c8c2202-8155-4b83-914b-236397238be7.png)
VPC sharing (part of Resource Access Manager) allows multiple AWS accounts to create their application resources such as EC2 instances, RDS databases, Redshift clusters, and Lambda functions, into shared and centrally-managed Amazon Virtual Private Clouds (VPCs).

To set this up, the account that owns the VPC (owner) shares one or more subnets with other accounts (participants) that belong to the same organization from AWS Organizations. After a subnet is shared, the participants can view, create, modify, and delete their application resources in the subnets shared with them. Participants cannot view, modify, or delete resources that belong to other participants or the VPC owner.

You can share Amazon VPCs to leverage the implicit routing within a VPC for applications that require a high degree of interconnectivity and are within the same trust boundaries. This reduces the number of VPCs that you create and manage while using separate accounts for billing and access control.

