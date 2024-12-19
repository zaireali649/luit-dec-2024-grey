from helpers import *
from typing import Any

def create_instances(ec2_client: Any, ami_type: str = "Linux 2023", instance_amount: int = 1) -> None:
    """
    Creates EC2 instances based on the specified AMI type and number of instances.

    Args:
        ec2_client (Any): The EC2 client used to interact with AWS services.
        ami_type (str): The AMI type to use for the instance. Options are 'Ubuntu', 'Linux 2023', and 'Linux 2'. Defaults to 'Linux 2023'.
        instance_amount (int): The number of instances to create. Defaults to 1.

    Returns:
        None
    """
    for i in range(instance_amount):
        # Check if the specified AMI type is 'Ubuntu'
        if ami_type.lower() == "ubuntu":
            create_ubuntu_instance(ec2_client)  # Create an Ubuntu instance
            print("Created Ubuntu Instance")
        # Check if the specified AMI type is 'Linux 2023'
        elif ami_type.lower() == "linux 2023":
            create_amazon_linux_2023_instance(ec2_client)  # Create an Amazon Linux 2023 instance
            print("Created Linux 2023 Instance")
        # Check if the specified AMI type is 'Linux 2'
        elif ami_type.lower() == "linux 2":
            create_amazon_linux_2_instance(ec2_client)  # Create an Amazon Linux 2 instance
            print("Created Linux 2 Instance")
        # Handle unsupported AMI types
        else:
            print("AMI type not supported")

# Example usage
# Obtain an EC2 client to interact with AWS services
ec2_client = get_ec2_client()

# Create 3 instances with the 'Linux 2' AMI
generate_instances(ec2_client, "Linux 2", instance_amount=3)

# Create 1 instance with the 'Ubuntu' AMI
generate_instances(ec2_client, ami_type="ubuNtu")

# Create 3 instances with the default 'Linux 2023' AMI
generate_instances(ec2_client, instance_amount=3)
