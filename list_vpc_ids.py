import boto3  # Import the Boto3 library for interacting with AWS services

# Initialize the EC2 client to interact with VPCs
vpc_client = boto3.client('ec2')

# Retrieve the list of VPCs in the AWS account
response = vpc_client.describe_vpcs()

# Extract the VPCs information from the response
vpcs = response['Vpcs']

# Iterate over each VPC and print its ID
for vpc in vpcs:
    print(vpc['VpcId'])
