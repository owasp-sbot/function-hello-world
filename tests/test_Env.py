import os
from unittest                    import TestCase
from function_hello_world.Env import Env

class test_Env(TestCase):

    def setUp(self):
        Env()

    def test_aws_credentials(self):
        assert type(os.environ['AWS_ACCESS_KEY_ID'    ]) is str
        assert type(os.environ['AWS_SECRET_ACCESS_KEY']) is str
        assert type(os.environ['AWS_SESSION_TOKEN'    ]) is str
