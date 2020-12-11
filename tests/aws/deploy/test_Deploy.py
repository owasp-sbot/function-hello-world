import os
from pprint import pprint
from unittest import TestCase

from osbot_aws.AWS_Config import AWS_Config
from osbot_aws.apis.IAM import IAM
from osbot_aws.apis.Lambda import Lambda
from osbot_aws.apis.test_helpers.Temp_Aws_Roles import Temp_Aws_Roles
from osbot_aws.helpers.Test_Helper import Test_Helper
from osbot_utils.utils.Files import folder_exists

from function_hello_world.aws.deploy.Deploy import Deploy
from function_hello_world.aws.lambdas.hello_world import run


class test_Deploy(TestCase):

    def setUp(self) -> None:
        self.deploy = Deploy(run)
        #Test_Helper().check_aws_token()
        self.aws_config = AWS_Config()

    def test__init__(self):

        assert self.deploy.deploy_lambda.lambda_name == self.deploy.deploy_lambda.handler.__module__
        assert self.deploy.deploy_lambda.role_arn == f"arn:aws:iam::{self.aws_config.aws_session_account_id()}:role/temp_role_for_lambda_invocation"
        assert type(self.deploy.deploy_lambda.handler).__name__ == 'function'

    def test_now__invoke(self):
        assert self.deploy.now()['status'] == 'ok'
        assert self.deploy.invoke()        ==  'From lambda code, hello None'

