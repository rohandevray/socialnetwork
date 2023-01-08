from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(max_length=500,null=True,blank=True)
    followers = models.IntegerField(null=True,blank=True,default=0)
    following =models.IntegerField(null=True,blank=True,default=0)
    total_posts = models.IntegerField(null=True,blank=True,default=0)
    username = models.CharField(max_length=200,null=True,blank=True)
    location =models.CharField(max_length=200, null= True, blank=True)
    short_intro = models.CharField(max_length=200, null= True, blank=True)
    profile_image = models.ImageField(null=True,blank=True,default="default.jpg")
    bio = models.TextField(null=True,blank=True)
    created =models.DateTimeField(auto_now_add=True)
    id= models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True,unique=True)
    def __str__(self):
        return str(self.username)

class Follower(models.Model):
    owner = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    follows = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    created =models.DateTimeField(auto_now_add=True)
    id= models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True,unique=True)
    def __str__(self):
        return str(self.owner.name)
    
