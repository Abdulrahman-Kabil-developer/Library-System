from django.db import models
from django.db.models.expressions import Value


# Create your models here.
class book(models.Model):
    title=models.CharField(max_length=100)
    ISBN=models.IntegerField(default=0)
    publishedAt=models.DateField(auto_now=True)
    borrowingPeriod=models.IntegerField(default=0)
    numberOfPages=models.IntegerField(default=0)
    author=models.CharField(max_length=100)
    image=models.ImageField()
    borowingStatu=models.BooleanField()
    description=models.TextField()

    def __str__(self):
        return self.title







