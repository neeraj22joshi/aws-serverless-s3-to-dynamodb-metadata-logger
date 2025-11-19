# 🛠️ Setup Instructions

# Step1️⃣: Create S3 Bucket
Name: neeraj-upload-bucket-demo
Region: ap-south-1

# Step2️⃣: Create DynamoDB Table
Name: UploadsMetadata
Partition Key: id (String)

# Step3️⃣: Create IAM Role for Lambda
Attach:
1. AWSLambdaBasicExecutionRole
2. AmazonDynamoDBFullAccess
Role Name → LambdaS3ToDynamoFullAccessRole

# Step4️⃣: Create Lambda Function
Name: S3MetadataWriter
Runtime: Python 3.10
Use IAM Role created above
Paste the code provided in S3MetadataWriter.py.

# Step5️⃣: Add S3 Trigger
S3 Bucket → neeraj-upload-bucket-demo
Event type → All object create events

# 🧪 Testing
Upload any file (txt/jpg/pdf) into S3 bucket.
Go to DynamoDB → UploadsMetadata → Items.
You’ll observe that S3 metadata logs are automatically generated and recorded in the table.

# 🩺 Debugging

View logs:
CloudWatch → Log groups → /aws/lambda/S3MetadataWriter

Common issues:
Wrong region
Trigger missing
IAM role missing DynamoDB access

# 🧼 Cleanup (to avoid charges)

Delete in this order:
Delete S3 bucket + contents
Delete Lambda function
Delete IAM role

Delete DynamoDB table
