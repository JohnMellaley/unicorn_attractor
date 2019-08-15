from django.test import TestCase, Client
from django.contrib.auth.models import User
from features.models import Feature

class TestViews(TestCase):
        
    def test_view_cart(self):
        page = self.client.get("/cart/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "cart.html")
    
    def test_add_to_cart(self):
        client = Client()
        self.user = User.objects.create_user('john10', 'admin@admin.com', 'john10')
        self.user.save()
        self.client.login(username="john10", password="john10")
        
        item = Feature(name="Create a Test featture",description="test description",  price=30.00, author=self.user)
        item.save()
                
        response = self.client.post("/cart/add/{0}".format(item.id),{
                'quantity':2,
                'author':self.user
        })
        #check after post, that redirect was call '302'
        self.assertEqual(response.status_code, 302)
        #redirect goes to /features/
        self.assertEqual(response.url, '/features/')
        
    def test_adjust_cart(self):
        client = Client()
        self.user = User.objects.create_user('john10', 'admin@admin.com', 'john10')
        self.user.save()
        self.client.login(username="john10", password="john10")
        
        item = Feature(name="Create a Test featture",description="test description",  price=30.00, author=self.user)
        item.save()
        
        response = self.client.post("/cart/adjust/{0}".format(item.id),{
                'quantity':2,
                'author':self.user
        })
        #check after post, that redirect was call '302'
        self.assertEqual(response.status_code, 302)
        #redirect goes to /features/
        self.assertEqual(response.url, '/cart/')