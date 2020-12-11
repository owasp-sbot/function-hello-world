from osbot_aws.AWS_Config import AWS_Config
from osbot_aws.OSBot_Setup import OSBot_Setup
from osbot_aws.apis.test_helpers.Temp_Aws_Roles import Temp_Aws_Roles
from osbot_aws.helpers.Lambda_Package import Lambda_Package

from function_hello_world.Env import Env
from osbot_aws.deploy.Deploy_Lambda import Deploy_Lambda

class Deploy:

    def __init__(self, handler):
        Env()
        self.deploy_lambda = Deploy_Lambda(handler)

    def now(self):
        return self.deploy_lambda.update()

    def invoke(self,params=None):
        return self.deploy_lambda.lambda_invoke(params)