from django import forms
from .models import Bug
from .models import Post

class BugForm(forms.ModelForm):

    class Meta:
        model = Bug
        fields = ('name', 'description')
        

class BlogPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'published_date')