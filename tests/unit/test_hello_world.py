from unittest import TestCase

from function_hello_world.hello_world import run


class test_hello_world(TestCase):

    def test_run(self):         # invoke lambda function directly (i.e. out side AWS)
        event   = {}
        context = {}
        assert run(event, context) == "From lambda code, hello None"

        event = { "name" : "world"}

        assert run(event, context) == "From lambda code, hello world"
