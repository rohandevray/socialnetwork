from django.forms import ModelForm
from .models import Profile

#for registering user
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','email','password1','password2']
        labels ={
            'first_name':'Name',
            'email':'Email'
        }

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name','email','location','bio','profile_image']