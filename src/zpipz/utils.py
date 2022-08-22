from dataclasses import dataclass
from pathlib import Path
from pkg_resources import get_distribution
from zpipz.errors import _CDKVersionError


ROOT_PATH = str(Path(".").resolve())


@dataclass
class DeployEnv:
    name: str
    stage: str
    index_alias: str
    index_model: str
    index_dataset: str


def check_cdk_version(pkg: str = "aws-cdk-lib", cfg: str = "pyproject.toml"):
    """ Checks if the the user's installed CDK version is compatible.

    :param pkg: Name of the AWS CDK Python package,
        defaults to 'aws-cdk-lib'
    :type pkg: str
    :param cfg: Location of a Python configuration file,
        defaults to 'pyproject.toml'
    :type cfg: str
    :raises _CDKVersionError: Error thrown when a non-compatible CDK version is
        installed.
    """
    installed_cdk_version = get_distribution(pkg).version
    desired_version = ""
    with open(Path(f"./{cfg}"), "r") as setup_file:
        lines = setup_file.readlines()
        for line in lines:
            if line.startswith(pkg):
                # handle semver checking
                check = line.split("=")[1].strip().strip('"')
                if check[0] == "~" or check[0] == "^":
                    desired_version = check[1:]
                elif check[0] == ">" or check[0] == "<":
                    desired_version = check[2:]
                else:
                    desired_version = check

    print(f"installed_cdk_version: {installed_cdk_version}")
    print(f"desired_version: {desired_version}")
    if installed_cdk_version != desired_version:
        raise _CDKVersionError(installed_cdk_version, desired_version)

