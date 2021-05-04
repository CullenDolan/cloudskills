# ask the user for an instance ID and autmoatically start it up

import boto3

ec2 = boto3.client('ec2')

def start_ec2instance(instanceID):
    ec2.start_instances(InstanceIds=[instanceID])

instanceID = input('What is the Instance ID you want to start? ')
start_ec2instance(instanceID)