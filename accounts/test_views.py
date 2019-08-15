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
        self.user = User.objects.create_user('john10', 'admin@admin.com', 'john10')
        self.user.save()
        self.client.login(username="john10", password="john10")
        page = self.client.get("/accounts/login/", follow = True)
        self.assertEqual(page.status_code, 200)
        self.assertRedirects(page, '/')
        self.assertTemplateUsed(page, "index.html")
        # message = list(page.context.get('messages'))[0]
        # self.assertEqual(message.tags, "success")
        # self.assertEqual(message.message, "You have successfully logged in")
        
    def test_get_login_page_post_incorrect_detials(self):
        self.user = User.objects.create_user('john10', 'admin@admin.com', 'john10')
        self.user.save()
        self.client.login(username="john10", password="john")
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
        # message = list(page.context.get('messages'))[0]
        # self.assertEqual(message.tags, "error")
        # self.assertEqual(message.message, "Your username or password is incorrect")
        
        
    def test_get_logout_page(self):
        self.user = User.objects.create_user('john10', 'admin@admin.com', 'john10')
        self.user.save()
        self.client.login(username="john10", password="john10")
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
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
        message = list(page.context.get('messages'))[0]
        self.assertEqual(message.tags, "success")
        self.assertEqual(message.message, "You have sucessfully registered")
        
    # def test_registration_with_user_already_regsitered(self):
    #     # post input to the register url
    #     client = Client()
    #     self.user = User.objects.create_user('john10', 'admin@admin.com', 'john10')
    #     self.user.save()
    #     self.client.login(username="john10", password="john10")
    #     page = self.client.post('/accounts/register/',
    #                             {'email': 'admin@admin.com',
    #                              'username': 'john10',
    #                              'password1': 'john10',
    #                              'password2': 'john10'})
        
        # self.assertEqual(page.status_code, 200)
        # self.assertTemplateUsed(page, "registration.html")
       
        
    def test_password_reset_form_page(self):
        page = self.client.get("/accounts/password-reset/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration/password_reset_form.html")
        
    def test_password_reset_done_page(self):
        page = self.client.get("/accounts/password-reset/done/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration/password_reset_done.html")
        
      
    # def test_password_reset_email_page(self):
    #     page = self.client.get("/accounts/register/")
    #     self.assertEqual(page.status_code, 200)
    #     self.assertTemplateUsed(page, "registration/password_reset_email.html")
        
    # def test_password_reset_confirm_page(self):
    #     token = response.context[0]['token']
    #     uid = response.context[0]['uid']
    #     page = self.client.get("/accounts/password-reset/, kwargs={'token':token,'uidb64':uid})")
    #     self.assertEqual(page.status_code, 200)
    #     self.assertTemplateUsed(page, "registration/password_reset_confirm.html")
        
    def test_password_reset_complete_page(self):
        page = self.client.get("/accounts/password-reset/complete/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration/password_reset_complete.html")

