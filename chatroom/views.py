from django.shortcuts import render ,redirect
from .models import MangaPost
from .forms import MangaPostForm , MangaCommentForm
from django.contrib import messages
# Create your views here.


def chatroom(request):
    context={}
    return render(request,'chatroom/rooms.html',context)


def mangaZ(request):
    posts = MangaPost.objects.all()
    form = MangaCommentForm()
    user_id = request.user.profile.id
    if request.method == "POST":
        form = MangaCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.owner = request.user.profile
            comment.save()
            messages.success(request,"Comment is successfully added!")
            return redirect("manga")
        
    context={'posts':posts,'form':form}
    return render(request,'chatroom/manga.html',context)

def codeMania(request):
    context={}
    return render(request,'chatroom/code.html',context)


def addPost(request):
    form = MangaPostForm()
    if request.method == "POST":
        form = MangaPostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user.profile
            
            post.save()
            return redirect("manga")
    context ={'form':form}
    return render(request,"chatroom/post-form.html",context)

# def addComment(request):
#     form = MangaCommentForm()
#     context ={'form':form}
#     return 
    