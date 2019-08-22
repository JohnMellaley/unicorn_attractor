from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UserLoginForm(forms.Form):
    """Form to be userd to log users in"""
    username =forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class UserRegistrationForm(UserCreationForm):
    """ for used to register a new user """
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput)
    password2 =forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput)
        
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # is statement so won't compare blank with exisint blank email
        if(email == ""):
            raise forms.ValidationError(u'User must submit an email')
        if (email != ""):
            username = self.cleaned_data.get('username')
            #check email is not already in the database
            if User.objects.filter(email=email).exclude(username=username):
                raise forms.ValidationError(u'Email must be unique')
        return email
        
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        # validate both passwird are entered   
        if not password1 or not password2:
            raise ValidationError("please confirm your password")
        #validate password must match   
        if password1 != password2:
            raise ValidationError("Passwords must match")
            
        return password2
        
    
        
        
        
        