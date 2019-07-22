from django import forms
from .models import Feature, PostFeature


class FeatureForm(forms.ModelForm):

    class Meta:
        model = Feature
        fields = ('name', 'description')
        
class BlogPostForm(forms.ModelForm):

    class Meta:
        model = PostFeature
        fields = ('title', 'content', 'published_date')