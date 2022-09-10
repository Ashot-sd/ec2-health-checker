import boto3ec2_client = boto3.client('ec2', region_name="eu_central-1")ec2_resource = boto3.resource('ec2', region_name="eu-central-1")statuses = ec2_client.describe_instance_status()for status in statuses['InstanceStatuses']:    ins_status = status['InstanceStatus']['Status']    sys_status = status['SystemStatus']['Status']    state = status['InstanceState']['Name']    print(f"Instance {status['InstanceId']} is {status} with instance status {ins_status} and system status {sys_status}")