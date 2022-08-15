class _CDKVersionError(Exception):
    """ Error thrown when a non-compatible CDK version is installed.

    :param v_installed: Version of AWS CDK the user installing this package has.
    :type v_required: str
    :param v_required: Minimum version of the AWS CDK required to install this
        package.
    :type v_required: str
    """
    def __init__(self, v_installed, v_required):
        print(f"Error: Found aws-cdk-lib {v_installed}, expected {v_required}")
