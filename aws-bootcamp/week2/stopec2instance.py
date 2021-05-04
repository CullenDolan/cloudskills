import boto3

ec2 = boto3.client('ec2')

def stop_ec2instance(instanceID):
    ec2.stop_instances(InstanceIds=[instanceID])

instanceID = input('What is the Instance ID you want to stop? ')
stop_ec2instance(instanceID)