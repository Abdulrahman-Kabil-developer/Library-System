from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify



# Create your models here.
borrowingStatuChoices=(
    ('Available','Available'),
    ('Un available','Un available'),
)
class book(models.Model):
    owner=models.ForeignKey(User,related_name='bookOwner',on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    ISBN=models.IntegerField(default=0)
    numberOfPages=models.IntegerField(default=0)
    description=models.TextField()
    borrowingPeriod=models.IntegerField(default=0)
    borowingStatu=models.CharField(max_length=20,choices=borrowingStatuChoices)
    publishedAt=models.DateField(auto_now=True)
    image=models.ImageField(upload_to='books/')
    slug=models.SlugField(blank=True,null=True)

    def save (self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(book,self).save(*args,**kwargs)


    def __str__(self):
        return self.title







