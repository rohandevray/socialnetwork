from django.forms import ModelForm
from .models import MangaPost ,MangaComment

class MangaPostForm(ModelForm):
    class Meta:
        model = MangaPost
        fields = ['title','description','post_image']
        labels ={
            'post_image':"image"
        }

class MangaCommentForm(ModelForm):
    class Meta:
        model = MangaComment
        fields = ['body']
        