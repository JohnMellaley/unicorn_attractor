from django.test import TestCase
from .models import Bug, Post
from django.contrib.auth.models import User


class TestBugModel(TestCase):

    def test_bug_add_with_defaults(self):
        author = User.objects.create(username='super', email='author@test.com')
        bug = Bug(name="Create a Test", description="test description", author= author)
        bug.save()
        self.assertEqual(bug.name, "Create a Test")
        self.assertEqual(bug.description, "test description")
        self.assertEqual(bug.vote, 0)
        self.assertEqual(bug.status, "q")
        
    def test_bug_add_without_defaults(self):
        author = User.objects.create(username='super', email='author@test.com')
        bug = Bug(name="Create a Test", description="test description", author= author, vote=1, status ='c')
        bug.save()
        self.assertEqual(bug.name, "Create a Test")
        self.assertEqual(bug.description, "test description")
        self.assertEqual(bug.vote, 1)
        self.assertEqual(bug.status, "c")
        
class TestPostModel(TestCase):
    def test_bug_add_with_defaults(self):
        author = User.objects.create(username='super', email='author@test.com')
        bug = Bug(name="Create a Test", description="test description", author=author)
        post = Post(title="Create a Test", content="test content", author= author, bugid=bug)
        self.assertEqual(post.title, "Create a Test")
        self.assertEqual(post.content, "test content")

        
    