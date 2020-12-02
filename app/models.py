from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=40)
    link = models.CharField(max_length=255)
    image = CloudinaryField('image',default="image.jpg")
    contentscore=models.IntegerField(default=0)
    creativityscore=models.IntegerField(default=0)
    userabilityscore=models.IntegerField(default=0)
    rating=models.IntegerField(default=0, validators=[
          MaxValueValidator(10),
          MinValueValidator(0)
    ])
     
    def __str__(self):
        return str(self.pk)

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    projects=models.ForeignKey(Project,on_delete=models.CASCADE)


    def __str__(self):
        self.username


    
