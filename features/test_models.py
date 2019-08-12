from django.test import TestCase
from .models import Feature, PostFeature
from django.contrib.auth.models import User


class TestFeatureModel(TestCase):

    def test_feature_add_with_defaults(self):
        author = User.objects.create(username='super', email='author@test.com')
        feature = Feature(name="Create a Test", description="test description", price=30.00, author= author)
        feature.save()
        self.assertEqual(feature.name, "Create a Test")
        self.assertEqual(feature.description, "test description")
        self.assertEqual(feature.price, 30.00)
        self.assertEqual(feature.vote, 0)
        self.assertEqual(feature.status, "q")
        
    def test_feature_add_without_defaults(self):
        author = User.objects.create(username='super', email='author@test.com')
        feature = Feature(name="Create a Test", description="test description", author= author, price=20.00, vote=1, status ='c')
        feature.save()
        self.assertEqual(feature.name, "Create a Test")
        self.assertEqual(feature.description, "test description")
        self.assertEqual(feature.price, 20.00)
        self.assertEqual(feature.vote, 1)
        self.assertEqual(feature.status, "c")
        
class TestPostModel(TestCase):
    def test_feature_add_with_defaults(self):
        author = User.objects.create(username='super', email='author@test.com')
        feature = Feature(name="Create a Test", description="test description", author=author)
        post = PostFeature(title="Create a Test", content="test content", author= author, featureid=feature)
        self.assertEqual(post.title, "Create a Test")
        self.assertEqual(post.content, "test content")