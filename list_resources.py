from typing import Any  # Import Any for type hints when specific AWS types are not available
from helpers import *  # Import helper functions for AWS operations

def print_bucket_names(s3_client: Any) -> None:
    """
    Fetches and prints the names of all S3 buckets accessible by the provided S3 client.

    Args:
        s3_client (Any): The AWS S3 client object used to interact with the S3 service.

    Returns:
        None
    """
    bucket_names = list_buckets(s3_client)  # Retrieve a list of bucket names using the helper function
    for bucket_name in bucket_names:
        print(bucket_name)  # Print each bucket name

def print_instance_ids(ec2_client: Any) -> None:
    """
    Fetches and prints the instance IDs of all EC2 instances accessible by the provided EC2 client.

    Args:
        ec2_client (Any): The AWS EC2 client object used to interact with the EC2 service.

    Returns:
        None
    """
    instances = describe_instances(ec2_client)  # Retrieve a list of instances using the helper function
    instance_ids = []  # Initialize a list to store instance IDs
    for instance in instances:
        instance_ids.append(instance['InstanceId'])  # Extract and append the instance ID
    for instance_id in instance_ids:
        print(instance_id)  # Print each instance ID

# Initialize AWS clients
ec2_client: Any = get_ec2_client()  # Retrieve EC2 client
s3_client: Any = get_s3_client()  # Retrieve S3 client

# Print names of S3 buckets
print_bucket_names(s3_client)

# Print IDs of EC2 instances
print_instance_ids(ec2_client)
