from django.test import TestCase
from .forms import  UserLoginForm, UserRegistrationForm
from django.contrib.auth.models import User
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
        
    def test_password_reset_form_page(self):
        page = self.client.get("/accounts/password-reset/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration/password_reset_form.html")
        
    def test_password_reset_done_page(self):
        page = self.client.get("/accounts/password-reset/done/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration/password_reset_done.html")
        
# HOW TO TEST AN EMAIL       
#    def test_password_reset_email_page(self):
#        page = self.client.get("/accounts/register/")
#        self.assertEqual(page.status_code, 200)
#        self.assertTemplateUsed(page, "registration/password_reset_email.html")
        
#Failed
#    def test_password_reset_confirm_page(self):
#        page = self.client.get("/accounts/password-reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/")
#        self.assertEqual(page.status_code, 200)
#        self.assertTemplateUsed(page, "registration/password_reset_confirm.html")
        
    def test_password_reset_complete_page(self):
        page = self.client.get("/accounts/password-reset/complete/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration/password_reset_complete.html")

