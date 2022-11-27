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
