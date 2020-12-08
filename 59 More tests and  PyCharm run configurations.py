# in blog.py file:

class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []


# in the tests folder: create blog_test.py file, and in it:

# from blog import Blog
from unittest import TestCase


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog("Test Title", "Test Author")

        self.assertEqual("Test Title", b.title)
        self.assertEqual("Test Author", b.author)
        self.assertListEqual([], b.posts)   # that's one way of doing it - the other is (because not all frameworks have assertListEqual implemented:
        # self.assertEqual(0 /or len[]/, len(b.posts))


# How to make sure the tests run if they don't match the default "test_*.py" format?
# Find unittest settings > Unittest in unit > Pattern > change the default pattern to "*_test.py" (or anything else with "test" in it)