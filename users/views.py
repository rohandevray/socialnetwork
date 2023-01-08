from django.shortcuts import render ,redirect
from .models import Profile
from feed.models import Post
#for register user form
from .forms import ProfileForm,CustomUserCreationForm
#for web authentication
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
# from .utils import createFollower
# Create your views here.

def loginUser(request):

    # if request.user.is_authenticated:
    #      return redirect("posts")
    
    if request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,"Something went wrong!")
        
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            print("logged in")
            messages.success(request,"Successfully logged in")
            return redirect(request.GET['next'] if 'next' in request.GET else 'posts') 

        else:
            messages.error(request,"Credientials are wrong!")

    return render(request,'users/login.html')

def registerUser(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request,"Account successfully created")
            login(request,user)
            return redirect("posts")
        else:
            messages.error(request,"something went wrong!")
    context={'form':form}
    return render(request,'users/register.html',context)

def logoutUser(request):
    logout(request)
    messages.info(request,"Successfully logged out!")
    return redirect("login")

def UserProfile(request,pk):
    profile = Profile.objects.get(id=pk) #for single element we use get
    posts = Post.objects.filter(owner_id=pk)
    posts_count = posts.__len__()
    context={'profile':profile,'posts_count':posts_count,'posts':posts}
    return render(request,'users/profile.html',context)


def updateProfile(request,pk):
    profile = Profile.objects.get(id=pk)
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect("user-profile",pk=profile.id)
    context ={'form':form,'profile':profile}
    return render(request,'users/update-profile.html',context)
