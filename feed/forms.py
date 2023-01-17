from django.forms import ModelForm
from .models import Post , Comment

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','description','posted_image']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['short_troll']
        labels ={
            'short_troll' : 'comment'
        }