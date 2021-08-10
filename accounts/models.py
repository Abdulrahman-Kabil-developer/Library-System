from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    nationalID=models.IntegerField(default=00000000000000)
    collageID=models.IntegerField(default=00000000)
    phoneNumber=models.CharField(max_length=13)
    city =models.ForeignKey('city',related_name='userCity',on_delete=models.CASCADE,blank=True,null=True)
    image=models.ImageField(upload_to='profile/')
    def __str__(self):
        return str(self.user)


@receiver (post_save, sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        profile.objects.create(user=instance)


class city(models.Model): 
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name


