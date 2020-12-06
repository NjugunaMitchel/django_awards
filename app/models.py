from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django import forms
from django.utils import timezone
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Project(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts',default="your username")
    image = CloudinaryField('image')
    name_of_site = models.CharField(max_length=255,default="site name")
    link = models.CharField(max_length=255)
    description = models.CharField(max_length=255,default='no profile')
    technologies = models.CharField(max_length=255,default="what technologies")
    def __str__(self):
        return self.name_of_site

    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images     

    def delete_project(self):
        self.delete()

    def save_project(self):
        self.save()


    @classmethod
    def search_by_name(cls, search_term):
        got_projects = Project.objects.filter(sitename__icontains=search_term)
        return got_projects

class Reviews(models.Model):
    RATES= (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    )
    username = models.ForeignKey(User, on_delete=models.CASCADE,)
    post = models.ForeignKey(Project, on_delete=models.CASCADE,)
    pub_date = models.DateTimeField(auto_now=True)
    userability_rating = models.IntegerField(default=1, choices=RATES, null=True)
    content_rating = models.IntegerField(default=1, choices=RATES, null=True)
    design_rating = models.IntegerField(default=1, choices=RATES, null=True)
    rating = models.CharField(max_length=200)

    def __str__(self):
        return self.rating

    def delete_review(self):
        self.delete()

    def save_review(self):
        self.save()

class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_photo = CloudinaryField('image', default='image.jpg')
    bio = models.CharField(blank=True,default='joined!', max_length = 255)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.user} profile'


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profiles.objects.create(user=instance)
           

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profiles.objects.create(user=instance)
   
    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()


    def save_profile(self):
        self.save() 

    def delete_profile(self):
        self.delete()

    def update_bio(self,new_bio):
        self.bio = new_bio
        self.save()

     

