from django.test import TestCase
from .forms import  UserLoginForm, UserRegistrationForm

# Create your tests here.
class TestloginformForm(TestCase):

    def test_can_login(self):
        form = UserLoginForm({'username':'johnmellaley','password':'ballybay'})
        self.assertTrue(form.is_valid())
    
    def test_correct_message_details_incorrect(self):
        form = UserLoginForm({'username':'','password':'ballybay'})
        self.assertEqual(form.errors['username'], [u'This field is required.'])
        
class TestUserRegistrationForm(TestCase):
    
    def test_can_register(self):
        form = UserRegistrationForm({'email':'email@gmail.com','username':'johnmellaley','password1':'ballybay','password2':'ballybay'})
        self.assertTrue(form.is_valid())
        
    def test_cannot_register_without_email(self):
        form = UserRegistrationForm({'email':'','username':'johnmellaley','password1':'ballybay','password2':'ballybay'})
        self.assertFalse(form.is_valid())
    
    def test_UserRegistrationForm_password_not_match(self):
        form = UserRegistrationForm(
            data={'email': "john@hotmail.com", 'username': "u",
                  'password1': "test", 'password2': "test1"})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'password2': ['Passwords must match']})
      
    def test_cannot_register_without_password1(self):
        form = UserRegistrationForm({'email':'','username':'johnmellaley','password1':'','password2':'ballybay'})
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors) #2 errors This field is required and please confirm your password

     
    