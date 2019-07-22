from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=254, default='')
    description =models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    vote = models.IntegerField(default=0)
    STATUS = (
        ('q','In Queue'),
        ('p','In Progress'),
        ('c','Completed'),
    )
    status = models.CharField(max_length=1, choices=STATUS, default='q')
    author = models.ForeignKey(User, default=None)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class UserFeature(models.Model):
    userid = models.ForeignKey(User, default=None)
    featureid = models.ForeignKey(Feature, default=None)
    
   
    class Meta: 
        unique_together = ('userid', 'featureid')
        
class PostFeature(models.Model):
    """
    A single Blog post
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    author = models.ForeignKey(User, default=None)
    featureid = models.ForeignKey(Feature, default=None)

    def __unicode__(self):
        return self.title