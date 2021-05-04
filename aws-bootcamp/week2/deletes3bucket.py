# show existing S3 buckets delete the one you dont want  
import boto3
import sys

def main():
    retrieve_s3_buckets()
    name = ask_for_bucket()
    delete_s3_bucket(name)
    
def retrieve_s3_buckets():
    """print out current buckets"""
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    print("Existing Buckets: ")
    for bucket in response['Buckets']:
        print(f'{bucket["Name"]}')


def delete_s3_bucket(name):
    """client function passes in the service you are interacting with"""
    client = boto3.client('s3')

    delete = client.delete_bucket(
        Bucket = name,
    )
    print(delete)

def ask_for_bucket():
    """get user input on which bucket to delete"""
    return input('Which S3 bucket do you want to delete? ')


if __name__ == '__main__':
    main()