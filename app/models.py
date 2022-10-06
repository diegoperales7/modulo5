from pyexpat import model
from django.db import models


class Sender(models.Model):
    fullName=models.CharField(max_length=200,unique=True) 
    ciNit=models.CharField(max_length=10,unique=True)
    phoneNumber=models.CharField(max_length=12)
    email=models.EmailField(max_length=250)
     
