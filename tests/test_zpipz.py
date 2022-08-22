from aws_cdk import (
    App,
    Environment,
    Stack,
)
from constructs import Construct

import os

test_app = App()
environment = Environment(
    region="us-east-1",
    account="123456789012",
    # region=os.environ["CDK_DEFAULT_REGION"],
    # account=os.environ["CDK_DEFAULT_ACCOUNT"],
)
namespace = "test-stack"

class DefaultS3Stack(Stack):
    def __init__(
        self, scope: Construct, construct_id: str, namespace: str, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        DefaultBucket(self, f"{namespace}-default-s3-bucket")


from zpipz.s3_bucket import DefaultBucket

s3_stack = DefaultS3Stack(
    test_app,
    f"{namespace}-default-s3-stack",
    namespace=namespace,
    env=environment,
)


test_app.synth()


def test_default_bucket_is_encrypted(stack):
    assert stack.encryption


test_default_bucket_is_encrypted(s3_stack)
            # encryption=s3.BucketEncryption.S3_MANAGED,  # S3 Managed encryption
            # server_access_logs_bucket=logging_bucket,
            # server_access_logs_prefix=logging_prefix,
            # block_public_access=s3.BlockPublicAccess.BLOCK_ALL,  # Public Access: BLOCK ALL # noqa: E501
            # removal_policy=removal_policy,
            # auto_delete_objects=auto_delete_objects,
            # versioned=True,
            # enforce_ssl=True,
            # **kwargs,
