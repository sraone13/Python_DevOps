import boto3

client = boto3.client('s3')

response = client.get_bucket_acl(
    Bucket='sravan-devops-bucket-20250421'
)
print(response)


#Project using the boto3 in Lambda function and cost optimization

# https://github.com/iam-veeramalla/aws-devops-zero-to-hero/tree/main/day-17
# https://github.com/iam-veeramalla/aws-devops-zero-to-hero/tree/main/day-18