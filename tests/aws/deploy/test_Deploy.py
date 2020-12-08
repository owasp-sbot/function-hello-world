from unittest import TestCase

from osbot_aws.apis.Lambda import Lambda
from osbot_aws.apis.test_helpers.Temp_Aws_Roles import Temp_Aws_Roles

from function_hello_world.aws.deploy.Deploy import Deploy


class test_Deploy(TestCase):

    def setUp(self) -> None:
        self.deploy = Deploy()

    def test__init__(self):
        assert self.deploy.lambda_name == 'hello_world'
        print()
        print(self.deploy.role_arn)

    def test_check_aws_role(self):
        self.deploy.check_aws_role()
        assert Temp_Aws_Roles().for_lambda_invocation__not_exists() is False

    # def test_deploy(self):
    #     print()
    #     self.deploy.check_aws_connection()
    #
    #     aws_lambda = Lambda().functions()
    #     print(aws_lambda)

