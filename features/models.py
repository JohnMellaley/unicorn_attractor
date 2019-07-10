from django.db import models
from django.contrib.auth.models import User

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
    
    def __str__(self):
        return self.name