from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Talaba(models.Model):
    image = models.ImageField(upload_to='profilepic')
    ism = models.CharField(max_length=200)
    familiya = models.CharField(max_length=200)
    yosh = models.IntegerField()
    kasb = models.CharField(max_length=200)
    
    def __str__(self):
        return self.ism
    