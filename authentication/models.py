from asyncio.windows_events import NULL
from django.db import models


STATUS_CHOICES = (
        ('Hot', 'Hot Lead'),
        ('Med', 'Med Lead'),
        ('Grey', 'Grey Lead'),
        ('New', 'New Lead'),
        ('Success', 'Success'),
        ('Mark Now', 'Mark Now'),
    )
# Create your models here.
class Lead(models.Model):
    first_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    id = models.IntegerField(primary_key=True,editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField( max_length=17, blank=True) 
    status = models.CharField(max_length=100, choices=STATUS_CHOICES,default=False)
    assigned_to = models.CharField(max_length=30,default='')
    #password =  models.CharField(max_length=20, default='')


class Remark(models.Model):
    id = models.IntegerField(primary_key=True,editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    remark = models.TextField(max_length=150)
    lead_id=models.ForeignKey(Lead,on_delete=models.CASCADE,default=NULL)
    


    
