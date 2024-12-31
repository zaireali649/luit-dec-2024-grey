import boto3  # Import the Boto3 library for interacting with AWS services

# Initialize the S3 client
s3 = boto3.client('s3')

# List all S3 buckets in the AWS account
response = s3.list_buckets()

# Extract the list of buckets from the response
buckets = response["Buckets"]

# Iterate over each bucket and print its name
for bucket in buckets:
    print(bucket["Name"])
