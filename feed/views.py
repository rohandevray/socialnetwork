from django.shortcuts import render ,redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required(login_url="login")
def Posts(request):
    profile = request.user.profile
    posts = Post.objects.all()
    context={'posts':posts,'profile':profile}
    return render(request,'feed/posts.html',context)

@login_required(login_url="login")
def addPost(request):
    profile = request.user.profile
    form= PostForm()
    if request.method == "POST":
        form= PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = profile
            post.save()
            messages.success(request,"Successfully posted!")
            return redirect("posts")
    context={'form':form,'profile':profile}
    return render(request,'feed/post-form.html',context)

@login_required(login_url="login")
def singlePost(request,pk):
    current_user = request.user.profile
    singlepost = Post.objects.get(id=pk)
    # cments = Comment.objects.filter(owner_id=singlepost.id)
    # form = CommentForm()
    # if request.method == "POST":
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         comment = form.save(commit=False)
    #         comment.owner = singlepost
    #         comment.bosse = current_user
    #         comment.save()
    #         return redirect("single-post", pk = singlepost.id)
    # singlepost.total_comments = cments.__len__()
    # singlepost.save() #updating total comments on db
    # total_comments = cments.__len__()
    context={'post':singlepost,'current_user':current_user}
    return render(request,'feed/single-post.html',context)

@login_required(login_url="login")
def deletePost(request,pk):
    post = Post.objects.get(id=pk)
    post.delete()
    messages.info(request,"Post was deleted!")
    return redirect("posts")

# @login_required(login_url="login")
# def deleteCmt(request,pk):
#     cmnt = Comment.objects.get(id=pk)
#     cmnt.delete()
#     return redirect("posts")