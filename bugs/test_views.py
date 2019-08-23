from django.test import TestCase, Client
from .forms import BugForm, BlogPostForm
from .models import Bug, Post
from django.contrib.auth.models import User
import json

class TestBugViews(TestCase):
        
        def test_view_all_bugs(self):
                page = self.client.get("/bugs/")
                self.assertEqual(page.status_code, 200)
                self.assertTemplateUsed(page, "bugs.html")

        def test_viewbug_page(self):
                #create user
                self.user = User.objects.create_user('john10', 'admin@admin.com', 'john10')
                self.user.save()
                #create bug
                bug = Bug(name="Create a Test bug",description="test description",  author=self.user)
                bug.save()
                #go to bug page with bugid
                page = self.client.get("/bugs/viewbug/{0}".format(bug.id))
                self.assertEqual(page.status_code, 200)
                self.assertTemplateUsed(page, "viewbug.html")
                
        def test_create_a_bugpage_get(self):
                page = self.client.get("/bugs/add")
                self.assertEqual(page.status_code, 200)
                self.assertTemplateUsed(page, "bug_form.html")
                
        def test_create_a_bug_post(self): 
                #create us and login
                client = Client()
                self.user = User.objects.create_user('john10', 'admin@admin.com', 'john10')
                self.user.save()
                self.client.login(username="john10", password="john10")
                #post bug details
                response = self.client.post("/bugs/add",{
                        'name':'bug',
                        'description':'desc',
                        'author':self.user
                })
                #check after post, that redirect was call '302'
                self.assertEqual(response.status_code, 302)
                #redirect goes to /bugs/
                self.assertEqual(response.url, '/bugs/')
                #check bug was created and details match against what was posted
                test_against = Bug.objects.get(name='bug')
                self.assertEqual(test_against.description, 'desc')
            
        def test_create_a_bugpost_page_get(self):
                self.user = User.objects.create_user('john10', 'admin@admin.com', 'john10')
                self.user.save()
                self.client.login(username="john10", password="john10")
                bug = Bug(name="Create a Test bug",description="test description",  author=self.user)
                bug.save()
                page = self.client.get("/bugs/create_post_bug/{0}".format(bug.id))
                self.assertEqual(page.status_code, 200)
                self.assertTemplateUsed(page, "blogpostform.html")
                
        def test_create_a_bugpost_post(self): 
                client = Client()
                self.user = User.objects.create_user('john10', 'admin@admin.com', 'john10')
                self.user.save()
                self.client.login(username="john10", password="john10")
                bug = Bug(name="Create a Test bug",description="test description",  author=self.user)
                bug.save()
                response = self.client.post("/bugs/create_post_bug/{0}".format(bug.id),{
                        'title':'post',
                        'content':'test post',
                        'published_date':'2020-06-06',
                        'author':self.user
                })
                #check after post, that redirect was call '302'
                self.assertEqual(response.status_code, 302)
                #redirect goes to /bugs/
                self.assertEqual(response.url, "/bugs/viewbug/{0}".format(bug.id))
                #check bug was created and details match against what was posted
                test_against = Post.objects.get(title='post')
                self.assertEqual(test_against.content, 'test post')
                
              
                