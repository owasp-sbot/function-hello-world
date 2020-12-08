from osbot_aws.Globals import Globals
from osbot_aws.apis.test_helpers.Temp_Aws_Roles import Temp_Aws_Roles

from function_hello_world.Env import Env


class Deploy:

    def __init__(self):
        Env()
        self.lambda_name = "hello_world"
        self.role_arn    = Temp_Aws_Roles().for_lambda_invocation__role_arn()

    def check_aws_role(self):
        pass
