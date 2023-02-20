from django.db import models
from users.models import Profile
import uuid
# Create your models here.

class MangaPost(models.Model):
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=200,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    post_image = models.ImageField(null=True,blank=True,default="default.jpg")
    total_upvotes = models.IntegerField(null=True,blank=True,default=0)
    total_downvotes = models.IntegerField(null=True,blank=True,default=0)
    created =models.DateTimeField(auto_now_add=True)
    id= models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True,unique=True)
    def __str__(self):
        return str(self.title)
    
    class Meta:
        ordering = ['-created']
    


    def upvote(self):
        self.total_upvotes = self.total_upvotes + 1
        return self.total_upvotes
    
    def downvote(self):
        self.total_downvotes = self.total_downvotes -1
        return self.total_downvotes
        
    @property
    def countVotes(self):
        votes = self.total_upvotes - self.total_downvotes
        if votes < 0:
            votes = 0
        return votes


class MangaComment(models.Model):
    post = models.ForeignKey(MangaPost,on_delete=models.CASCADE,null=True,blank=True)
    owner = models.OneToOneField(Profile,on_delete=models.CASCADE,null=True,blank=True)
    body = models.CharField(max_length=500,null=True,blank=True)
    created =models.DateTimeField(auto_now_add=True)
    id= models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True,unique=True)
    def __str__(self):
        return self.owner.name
    
    class Meta:
        ordering =['-created']

    

