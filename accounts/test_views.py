from django.test import TestCase, Client
from .forms import  UserLoginForm, UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages

# from .models import Item

class TestViews(TestCase):

    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
    
    def test_get_login_page(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
        
    def test_get_login_page_post(self):
        #create user
        self.user = User.objects.create_user('john10', 'admin@admin.com', 'john10')
        self.user.save()
        #post details from login page
        page = self.client.post('/accounts/login/',
                                {'username': 'john10',
                                 'password':"john10"},follow=True)
        # test user goes to home page if detials correct
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
        #check correct message is displayed
        message = list(page.context.get('messages'))[0]
        self.assertEqual(message.tags, "success")
        self.assertEqual(message.message, "You have successfully logged in")
        
        
    def test_get_login_page_post_incorrect_detials(self):
        self.user = User.objects.create_user('john10', 'admin@admin.com', 'john10')
        self.user.save()
        #post incorrect detials
        page = self.client.post('/accounts/login/',
                                {'username': 'john10',
                                 'password':"john"},follow=True)
        #check user stays on login page                         
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
        #check error message
        message = list(page.context.get('messages'))[0]
        self.assertEqual(message.tags, "error")
        self.assertEqual(message.message, "Your username or password is incorrect")
        
    def test_get_logout_page(self):
        self.user = User.objects.create_user('john10', 'admin@admin.com', 'john10')
        self.user.save()
        self.client.login(username="john10", password="john10")
        # check page is redirect to index page
        page = self.client.get("/accounts/logout/", follow = True)
        self.assertEqual(page.status_code, 200)
        self.assertRedirects(page, '/')
        self.assertTemplateUsed(page, "index.html")

    def test_get_profile_page(self):
        self.user = User.objects.create_user('john10', 'admin@admin.com', 'john10')
        self.user.save()
        self.client.login(username="john10", password="john10")
        page = self.client.get("/accounts/profile/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")
    
    def test_statistics_page(self):
        page = self.client.get("/accounts/statistics/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "dashboard.html")
	
        
    def test_get_registration_page(self):
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration.html")
        
    def test_get_registration_post(self):
        # post input to the register url
        page = self.client.post('/accounts/register/',
                                {'email': 'paul@email.com',
                                 'username': 'paul',
                                 'password1': 'paul',
                                 'password2': 'paul'},
                                follow=True)
        #check user redirected to home page
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
        #check message is correct
        message = list(page.context.get('messages'))[0]
        self.assertEqual(message.tags, "success")
        self.assertEqual(message.message, "You have sucessfully registered")
        
    def test_password_reset_form_page(self):
        page = self.client.get("/accounts/password-reset/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration/password_reset_form.html")
        
    def test_password_reset_done_page(self):
        page = self.client.get("/accounts/password-reset/done/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration/password_reset_done.html")
        
    def test_password_reset_complete_page(self):
        page = self.client.get("/accounts/password-reset/complete/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration/password_reset_complete.html")

