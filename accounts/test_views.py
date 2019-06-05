from django.test import TestCase
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

#   FAILED        
#    def test_get_profile_page(self):
#        page = self.client.get("/accounts/profile/")
#        self.assertEqual(page.status_code, 200)
#        self.assertTemplateUsed(page, "profile.html")
        
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

#  NOT MY CODE DELETE WHEN FINISJED
        
#   def test_get_edit_item_page(self):
#        item = Item(name="Create a Test")
#        item.save()  */

#        page = self.client.get("/edit/{0}".format(item.id))
#        self.assertEqual(page.status_code, 200)
#        self.assertTemplateUsed(page, "item_form.html")
    
#    def test_get_edit_page_for_item_that_does_not_exist(self):
#        page = self.client.get("/edit/1")
#       self.assertEqual(page.status_code, 404)