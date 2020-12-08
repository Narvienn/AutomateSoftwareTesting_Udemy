from unittest import TestCase
# from post import Post


# The class from previous lesson
class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        pass # TBA

# The method for converting posts to JSONs (e.g. to commit them to a DB)
    def json(self):
        return {
            "title": self.title,        # converts a Post() object into a JSON/dictionary
            "content": self.content,    # trailing comma - can be useful fo when you're adding new lines
        }


class PostTest(TestCase):
    def test_create_post(self):
        p = Post("Test Title", "Test Content")

        self.assertEqual("Test Title", p.title)
        self.assertEqual("Test Content", p.content)

    def test_json(self):
        p = Post("Test Title", "Test Content")
        expected = {
            "title" : "Test Title",
            "content": "Test Content",
        }
    # assertDictEqual - asserts if dict keys and values are the same, not objects (keys and values may refer to different objects)
        self.assertDictEqual(expected, p.json())


        