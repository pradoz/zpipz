from aws_cdk import (
    App,
    Environment,
    Stack,
)
from aws_cdk.assertions import (
    Match,
    Matcher,
    Template,
)
from constructs import Construct
import pytest

from utils import get_template

test_app = App()
environment = Environment(
    region="us-east-1",
    account="123456789012",
    # region=os.environ["CDK_DEFAULT_REGION"],
    # account=os.environ["CDK_DEFAULT_ACCOUNT"],
)
namespace = "test"


class DefaultStack(Stack):
    def __init__(
        self, scope: Construct, construct_id: str, namespace: str, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.dft_bucket = DefaultBucket(self, f"{namespace}-default-s3-bucket")


from zpipz.s3_bucket import DefaultBucket

s3_stack = DefaultStack(
    test_app,
    f"{namespace}-default-stack",
    namespace=namespace,
    env=environment,
)

@pytest.fixture
def s3_stack_template() -> Template:
    t = get_template(s3_stack)
    return t


def test_default_bucket_uses_server_side_encryption(s3_stack_template: Template) -> None:
    s3_stack_template.has_resource_properties(
        type="AWS::S3::Bucket",
        props={
            "BucketEncryption": Match.object_equals({
                "ServerSideEncryptionConfiguration": Match.array_equals([
                    Match.object_equals({
                        "ServerSideEncryptionByDefault": Match.object_equals({
                            "SSEAlgorithm": Match.any_value(),
                        })
                    })
                ]),
            })
        },
    )

def test_default_bucket_blocks_all_public_access(s3_stack_template: Template) -> None:
    s3_stack_template.has_resource_properties(
        type="AWS::S3::Bucket",
        props={
            "PublicAccessBlockConfiguration": Match.object_equals({
                "BlockPublicAcls": True,
                "BlockPublicPolicy": True,
                "IgnorePublicAcls": True,
                "RestrictPublicBuckets": True
            })
        },
    )

def test_default_bucket_has_versioning_enabled(s3_stack_template: Template) -> None:
    s3_stack_template.has_resource_properties(
        type="AWS::S3::Bucket",
        props={
            "VersioningConfiguration": Match.object_equals({
                "Status": "Enabled"
            })
        }
    )

