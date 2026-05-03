import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    print("EVENT:", json.dumps(event))

    try:
        bucket_name = event['detail']['requestParameters']['bucketName']

        # Block public access
        s3.put_public_access_block(
            Bucket=bucket_name,
            PublicAccessBlockConfiguration={
                'BlockPublicAcls': True,
                'IgnorePublicAcls': True,
                'BlockPublicPolicy': True,
                'RestrictPublicBuckets': True
            }
        )

        # Delete bucket policy
        try:
            s3.delete_bucket_policy(Bucket=bucket_name)
        except Exception as e:
            print("No policy or error:", str(e))

        print("Fixed bucket:", bucket_name)

        return {"statusCode": 200}

    except Exception as e:
        print("ERROR:", str(e))
        return {"statusCode": 500}
