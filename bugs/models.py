from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# from django.contrib.auth import get_user_model



# Create your models here.
class Bug(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    vote = models.IntegerField(default=0)
    STATUS = (
        ('q','In Queue'),
        ('p','In Progress'),
        ('c','Completed'),
    )
    status = models.CharField(max_length=1, choices=STATUS, default='q')
    author = models.ForeignKey(User, default=None)
    
    def __str__(self):
        return self.name
        
class UserBug(models.Model):
    userid = models.ForeignKey(User, default=None)
    bugid = models.ForeignKey(Bug, default=None)
    
   
    class Meta: 
        unique_together = ('userid', 'bugid')
        
class Post(models.Model):
    """
    A single Blog post
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    author = models.ForeignKey(User, default=None)
    bugid = models.ForeignKey(Bug, default=None)

    def __unicode__(self):
        return self.title
    