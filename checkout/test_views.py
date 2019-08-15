from django.test import TestCase, Client
from django.contrib.auth.models import User
from features.models import Feature
from django.conf import settings
from django.contrib import messages


class TestViews(TestCase):
        
    def test_checkout_with_login_get(self):
        client = Client()
        self.user = User.objects.create_user('john10', 'admin@admin.com', 'john10')
        self.user.save()
        self.client.login(username="john10", password="john10")
        page = self.client.get("/checkout/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "checkout.html")
       
    def test_checkout_without_login_get(self): 
        page = self.client.get("/checkout/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
    
    def test_checkout_with_login_post(self):
        client = Client()
        self.user = User.objects.create_user('john10', 'admin@admin.com', 'john10')
        self.user.save()
        self.client.login(username="john10", password="john10")
        
        item = Feature(name="Create a Test feature",description="test description",  price=30.00, author=self.user)
        item.save()
        
        self.client.post("/cart/add/{0}".format(item.id),
                         data={'quantity': '6','author':self.user},
                         follow=True)
                         
        # assign the stripe publishable key to stripe_id
        stripe_id = 'tok_visa'
        
        page = self.client.post("/checkout/",
                                {'full_name': 'john',
                                 'phone_number': '123456789111',
                                 'street_address1': 'home',
                                 'street_address2': 'and dry',
                                 'town_or_city': 'bay',
                                 'county': 'dublin',
                                 'country': 'ireland',
                                 'postcode': 'eircode',
                                 'credit_card_number': '4242424242424242',
                                 'cvv': '111',
                                 'expiry_month': '6',
                                 'expiry_year': '2020',
                                 'stripe_id': stripe_id},
                                follow=True)
        
        #check after post, that redirect was call '302'
        self.assertEqual(page.status_code, 200)
        self.assertRedirects(page, '/features/')
        self.assertTemplateUsed(page, "features.html")
        message = list(page.context.get('messages'))[0]
        self.assertEqual(message.tags, "success")
        self.assertEqual(message.message, "You have successfully paid")
        
    def test_checkout_with_login_card_declined(self):
        client = Client()
        self.user = User.objects.create_user('john10', 'admin@admin.com', 'john10')
        self.user.save()
        self.client.login(username="john10", password="john10")
        
        item = Feature(name="Create a Test feature",description="test description",  price=30.00, author=self.user)
        item.save()
        
        self.client.post("/cart/add/{0}".format(item.id),
                         data={'quantity': '6','author':self.user},
                         follow=True)
                         
        # assign the stripe publishable key to stripe_id
        stripe_id = 'tok_chargeDeclined'
        
        page = self.client.post("/checkout/",
                                {'full_name': 'john',
                                 'phone_number': '123456789111',
                                 'street_address1': 'home',
                                 'street_address2': 'and dry',
                                 'town_or_city': 'bay',
                                 'county': 'dublin',
                                 'country': 'ireland',
                                 'postcode': 'eircode',
                                 'credit_card_number': '4000000000000002',
                                 'cvv': '111',
                                 'expiry_month': '6',
                                 'expiry_year': '2020',
                                 'stripe_id': stripe_id},
                                follow=True)
        
        #check after post, that redirect was call '302'
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "checkout.html")
        message = list(page.context.get('messages'))[0]
        self.assertEqual(message.tags, "error")
        self.assertEqual(message.message, "Your card was declined!")
        