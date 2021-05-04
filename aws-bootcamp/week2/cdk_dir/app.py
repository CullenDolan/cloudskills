#!/usr/bin/env python3

from aws_cdk import core
from cdk_dir.cdk_dir_stack import CdkDirStack
import aws_cdk.aws_s3 as s3


class S3(core.Stack):
    def S3Stack(self):
        s3.Bucket(
            bucket_name="cullencloudskilltest"
        )

app = core.App()
S3(app, "cdk")

# creates a cloudformation template
app.synth()