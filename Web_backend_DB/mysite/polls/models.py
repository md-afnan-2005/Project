from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=200)
    email_id = models.CharField(max_length=200)
    std_id = models.IntegerField(default=0)
    mob_no = models.IntegerField(default=0)
   
    