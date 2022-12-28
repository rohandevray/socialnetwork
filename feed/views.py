from django.shortcuts import render ,redirect
from .models import Post,Comment
from .forms import PostForm
# Create your views here.

def Posts(request):
    profile = request.user.profile
    posts = Post.objects.all()
    context={'posts':posts,'profile':profile}
    return render(request,'feed/posts.html',context)

def addPost(request):
    profile = request.user.profile
    form= PostForm()
    if request.method == "POST":
        form= PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = profile
            post.save()
            return redirect("posts")
    context={'form':form}
    return render(request,'feed/post-form.html',context)


def singlePost(request,pk):
    singlepost = Post.objects.get(id=pk)
    cments = Comment.objects.filter(owner_id=singlepost.id)
    if request.method == "POST":
        print("HELLO")
    singlepost.total_comments = cments.__len__()
    singlepost.save() #updating total comments on db
    total_comments = cments.__len__()
    context={'post':singlepost,'cments':cments,'total_comments':total_comments}
    return render(request,'feed/single-post.html',context)
