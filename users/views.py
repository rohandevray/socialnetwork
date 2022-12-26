from django.shortcuts import render
from .models import Profile
from feed.models import Post
# Create your views here.

def UserProfile(request,pk):
    profile = Profile.objects.get(id=pk) #for single element we use get
    posts = Post.objects.filter(owner_id=pk)
    posts_count = posts.__len__()
    context={'profile':profile,'posts_count':posts_count,'posts':posts}
    return render(request,'users/profile.html',context)
