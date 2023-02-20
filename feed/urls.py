from django.urls import path
from . import views



urlpatterns = [
    path('',views.Posts,name="posts"), #home page
    path('post-form/',views.addPost,name="post-form"),
    path('post/<str:pk>/',views.singlePost,name="single-post"),
    path('delete/<str:pk>/',views.deletePost,name="delete"),
    # path('del/<str:pk>/',views.deleteCmt,name="delete-cmt")
]