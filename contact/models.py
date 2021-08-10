from django.db import models

# Create your models here.

class Info (models.Model):
    place=models.CharField(max_length=50)
    phoneNumber=models.CharField(max_length=20)
    email=models.EmailField(max_length=254)
    description=models.TextField(max_length=500)
    
    def __str__(self) :
        return self.email


