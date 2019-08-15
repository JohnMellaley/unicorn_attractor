from django.test import TestCase, Client
from .forms import FeatureForm, BlogPostForm
from .models import Feature, PostFeature
from django.contrib.auth.models import User


class TestViews(TestCase):
        
        def test_view_all_features(self):
                page = self.client.get("/features/")
                self.assertEqual(page.status_code, 200)
                self.assertTemplateUsed(page, "features.html")

        def test_viewfeature_page(self):
                self.user = User.objects.create_user('john10', 'admin@admin.com', 'john10')
                self.user.save()
                feature = Feature(name="Create a Test featture",description="test description",  price=30.00, author=self.user)
                feature.save()
                page = self.client.get("/features/viewfeature/{0}".format(feature.id))
                self.assertEqual(page.status_code, 200)
                self.assertTemplateUsed(page, "viewfeature.html")
                
        def test_create_a_featurepage_get(self):
                page = self.client.get("/features/create_feature")
                self.assertEqual(page.status_code, 200)
                self.assertTemplateUsed(page, "feature_form.html")
                
        def test_create_a_feature_post(self):   
                client = Client()
                self.user = User.objects.create_user('john10', 'admin@admin.com', 'john10')
                self.user.save()
                self.client.login(username="john10", password="john10")
                
                response = self.client.post("/features/create_feature",{
                        'name':'feature',
                        'description':'desc',
                        'price':30.00,
                        'author':self.user
                })
                #check after post, that redirect was call '302'
                self.assertEqual(response.status_code, 302)
                #redirect goes to /features/
                self.assertEqual(response.url, '/features/')
                #check bug was created and details match against what was posted
                test_against = Feature.objects.get(name='feature')
                self.assertEqual(test_against.description, 'desc')
            
        def test_create_a_featurepost_page_get(self):
                self.user = User.objects.create_user('john10', 'admin@admin.com', 'john10')
                self.user.save()
                self.client.login(username="john10", password="john10")
                feature = Feature(name="Create a Test featture",description="test description",  price=30.00, author=self.user)
                feature.save()
                page = self.client.get("/features/create_post/{0}".format(feature.id))
                self.assertEqual(page.status_code, 200)
                self.assertTemplateUsed(page, "blogpostform.html")
                
        def test_create_a_featurepost_post(self): 
                client = Client()
                self.user = User.objects.create_user('john10', 'admin@admin.com', 'john10')
                self.user.save()
                self.client.login(username="john10", password="john10")
                feature = Feature(name="Create a Test feature",description="test description", price=30.00, author=self.user)
                feature.save()
                response = self.client.post("/features/create_post/{0}".format(feature.id),{
                        'title':'post',
                        'content':'test post',
                        'published_date':'2020-06-06',
                        'author':self.user
                })
                #check after post, that redirect was call '302'
                self.assertEqual(response.status_code, 302)
                #redirect goes to /bugs/
                self.assertEqual(response.url, "/features/viewfeature/{0}".format(feature.id))
                #check bug was created and details match against what was posted
                test_against = PostFeature.objects.get(title='post')
                self.assertEqual(test_against.content, 'test post')