from django.db import models
from users.models import Profile
import uuid

# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=200,null=True,blank=True)
    description = models.CharField(null=True,blank=True,max_length=500)
    posted_image = models.ImageField(null=True,blank=True,default="default.jpg")
    total_likes = models.IntegerField(null=True,blank=True,default=0)
    total_comments = models.IntegerField(null=True,blank=True,default=0)
    created =models.DateTimeField(auto_now_add=True)
    id= models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True,unique=True)
    def __str__(self):
        return self.title
    
    @property
    def addlike(self):
        self.total_likes = self.total_likes + 1
        return self.total_likes


class Comment(models.Model):
    owner = models.ForeignKey(Post,on_delete=models.CASCADE,null=True,blank=True)
    short_troll = models.CharField(max_length=400,null=True,blank=True)
    total_likes = models.IntegerField(null=True,blank=True,default=0)
    created =models.DateTimeField(auto_now_add=True)
    id= models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True,unique=True)
    def __str__(self):
        return str(self.owner)
