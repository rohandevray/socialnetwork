from django.forms import ModelForm
from .models import MangaPost

class MangaPostForm(ModelForm):
    class Meta:
        model = MangaPost
        fields = ['description','post_image']
        labels ={
            'post_image':"image"
        }
