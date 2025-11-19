## 📦 AWS Resources (exact names required)

| Resource | Name |
|---------|------|
| **S3 Bucket** | `neeraj-upload-bucket-demo` |
| **DynamoDB Table** | `UploadsMetadata` |
| **IAM Role** | `LambdaS3ToDynamoFullAccessRole` |
| **Lambda Function** | `S3MetadataWriter` |
| **Lambda Runtime** | Python 3.10 |

---

## 📄 Lambda Function Code

`/lambda/S3MetadataWriter.py`

```python
import json
import boto3
import uuid
 
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UploadsMetadata')
 
def lambda_handler(event, context):
    # This Lambda expects S3 PutObject-style event records
    for record in event.get('Records', []):
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        size = record['s3']['object'].get('size', 0)
        event_name = record.get('eventName')
        event_time = record.get('eventTime')
 
        item_id = str(uuid.uuid4())
 
        table.put_item(
            Item={
                'id': item_id,
                'bucket': bucket,
                'key': key,
                'size': int(size),
                'event_name': event_name,
                'event_time': event_time
            }
        )
 
    return {
        'statusCode': 200,
        'body': json.dumps('Metadata stored successfully!')
    }

