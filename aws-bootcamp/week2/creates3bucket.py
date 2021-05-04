# creat an S3 bucket 
import boto3
import sys

def main():
    create_s3_bucket(name)
    

def create_s3_bucket(name):
    # client function passes in the service you are interacting with
    client = boto3.client('s3')

    create = client.create_bucket(
        ACL = 'private', # access control list
        Bucket = name,
    )
    print(create)

name = input('What unique name do you want to call your S3 bucket? ')




if __name__ == '__main__':
    main()