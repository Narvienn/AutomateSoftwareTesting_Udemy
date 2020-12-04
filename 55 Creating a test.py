# First, create the object/function you want to test:

class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content


# Second, think if your object/function is a standalone or has any dependencies (other objects, functions, DB, interfaces etc.)
# Any class or function that does not depend on other things, you want to put it in your unit tests

# Go to tests folder, create a Python package called unit and create a Python file in it for the tested class/function etc. (e.g. post_test.py)
# In Python, each TS is a class, so in post_test.py, do sth like this:

from unittest import TestCase
# from post import Post - this would be in separate file, remember?

class PostTest(TestCase):
    def test_create_post(self):         # every test case will be a separate class method + the name has to start with 'test_'
        p = Post('Test', 'TestContent')
        self.assertEqual('Test', p.title)   # assert that 'Test' == p.title
        self.assertEqual('TestContent', p.content)


