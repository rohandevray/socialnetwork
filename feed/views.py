from django.shortcuts import render ,redirect
from .models import Post,Comment
# Create your views here.

def Posts(request):
    posts = Post.objects.all()
    context={'posts':posts}
    return render(request,'feed/posts.html',context)

def addPost(request):
    context={}
    return render(request,'feed/post-form.html',context)


def singlePost(request,pk):
    singlepost = Post.objects.get(id=pk)
    cments = Comment.objects.filter(owner_id=singlepost.id)
    if request.method == "POST":
        print('hello')
    singlepost.total_comments = cments.__len__()
    singlepost.save() #updating total comments on db
    total_comments = cments.__len__()
    context={'post':singlepost,'cments':cments,'total_comments':total_comments}
    return render(request,'feed/single-post.html',context)