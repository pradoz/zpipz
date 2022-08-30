from aws_cdk import (
    Stack,
)
from aws_cdk.assertions import (
    Template,
)


def get_template(stack: Stack) -> Template:
    t = Template.from_stack(stack)
    return t
