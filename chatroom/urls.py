from django.urls import path
from . import views

urlpatterns = [
    path('',views.chatroom,name="rooms"),
    path('code/',views.codeMania,name="code"),
    path('manga/',views.mangaZ,name="manga"),
    path('add-post/',views.addPost,name="add-post"),
]