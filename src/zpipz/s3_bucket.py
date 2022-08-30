"""Base-classes for S3 buckets deployed in commercial and ISO regions.
"""

from typing import Optional

from aws_cdk import (
    RemovalPolicy,
    aws_s3 as s3,
)
from constructs import Construct


class DefaultBucket(s3.Bucket):
    """ Default S3 Bucket.

    :param encryption: The encryption algorithm used on the S3 bucket,
        defaults to S3_MANAGED
    :type encryption: s3.BucketEncryption
    :param block_public_access: S3 Block Public Access mode,
        defaults to BLOCK_ALL
    :type block_public_access: s3.BlockPublicAccess
    :param auto_delete_objects: Whether the S3 Objects in this bucket should be
        deleted along with the CloudFormation stack,
        defaults to True
    :type auto_delete_objects: bool
    :param cfg: Location of a Python configuration file,
        defaults to 'pyproject.toml'
    :type cfg: RemovalPolicy
    :param logging_prefix: S3 prefix to store logs,
        defaults to None
    :type logging_prefix: str, optional
    :param logging_bucket: S3 bucket to store logs,
        defaults to None
    :type logging_bucket: s3.IBucket, optional
    :raises _CDKVersionError: Error thrown when a non-compatible CDK version is
        installed.
    """
    def __init__(
        self,
        scope: Construct,
        id: str,
        encryption=s3.BucketEncryption.S3_MANAGED,
        block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
        auto_delete_objects: bool = False,
        removal_policy: RemovalPolicy = RemovalPolicy.RETAIN,
        logging_prefix: Optional[str] = None,
        logging_bucket: Optional[s3.IBucket] = None,
        **kwargs,
    ):
        super().__init__(
            scope,
            id,
            encryption=encryption,
            block_public_access=block_public_access,
            server_access_logs_bucket=logging_bucket,
            server_access_logs_prefix=logging_prefix,
            removal_policy=removal_policy,
            auto_delete_objects=auto_delete_objects,
            versioned=True,
            enforce_ssl=True,
            **kwargs,
        )

        self.encryption = encryption
        self.server_access_logs_bucket = logging_bucket
        self.server_access_logs_prefix = logging_prefix
        self.block_public_access = block_public_access
        self.removal_policy = removal_policy
        self.auto_delete_objects = auto_delete_objects
        self.versioned = True
        self.enforce_ssl = True
