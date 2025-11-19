# Serverless S3 → Lambda → DynamoDB Metadata Logging Pipeline

A serverless data-ingestion pipeline built on AWS that automatically records S3 object metadata into DynamoDB using AWS Lambda.

This project demonstrates event-driven architecture, IAM permissions, DynamoDB integration, and Lambda triggers — created entirely via the AWS Console.

---

## 🚀 Features
- Automatically logs metadata for every file uploaded to S3  
- Serverless & fully managed  
- Real-time event processing via Lambda  
- DynamoDB used as a scalable, NoSQL metadata store  
- CloudWatch integration for monitoring and debugging  

---

## 🏗️ Architecture Overview

**Flow:**
1. File uploaded → `neeraj-upload-bucket-demo` (S3)  
2. S3 emits an `ObjectCreated` event  
3. Event triggers Lambda → `S3MetadataWriter`  
4. Lambda extracts metadata  
5. Lambda writes metadata into DynamoDB table → `UploadsMetadata`  
6. Logs stored in CloudWatch  

