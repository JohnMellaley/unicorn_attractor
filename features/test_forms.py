from django.test import TestCase
from .forms import FeatureForm,BlogPostForm

# Create your tests here.
class TestFeatureFormForm(TestCase):

    def test_can_add(self):
        form = FeatureForm({'name':'test','description':'test now'})
        self.assertTrue(form.is_valid())
    
    def test_name_is_blank(self):
        form = FeatureForm({'name':'','description':'ballybay'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])
        
    def test_description_is_blank(self):
        form = FeatureForm({'name':'john','description':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['description'], [u'This field is required.'])
        
class TestBlogPostForm(TestCase):
    
    def test_can_post_blog(self):
        form = BlogPostForm({'title':'mycomment','content':'johnmellaley','published_date':'05/08/2019'})
        self.assertTrue(form.is_valid())
    
    def test_blank_title_blog(self):
        form = BlogPostForm({'title':'','content':'johnmellaley','published_date':'05/08/2019'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], [u'This field is required.'])
        
    
    def test_invalid_date_blog(self):
        form = BlogPostForm({'title':'mycomment','content':'johnmellaley','published_date':'ballybay'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['published_date'], [u'Enter a valid date/time.'])