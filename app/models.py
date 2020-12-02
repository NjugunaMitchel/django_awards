from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=40)
    link = models.CharField(max_length=255)
    image = CloudinaryField('image',default="image.jpg")
    
class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    projects=models.ForeignKey(Project,on_delete=models.CASCADE)


    def __str__(self):
        self.username


    
