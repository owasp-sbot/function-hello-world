from unittest import TestCase

from function_hello_world.aws.deploy.Deploy import Deploy


class test_Deploy(TestCase):

    def setUp(self) -> None:
        self.deploy = Deploy()

    def test__init__(self):
        assert self.deploy.lambda_name == 'hello_world'