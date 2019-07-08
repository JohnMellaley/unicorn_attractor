from django.db import models
from django.contrib.auth.models import User
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
#        models.ForeignKey(
#      get_user_model(),
#      on_delete=models.CASCADE
#   )
    
   
    def __str__(self):
        return self.name
        
class UserBug(models.Model):
    userid = models.ForeignKey(User, default=None)
    bugid = models.ForeignKey(Bug, default=None)
    
   
    class Meta: 
        unique_together = ('userid', 'bugid')
        
    