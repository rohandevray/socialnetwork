from django.urls import path
from . import views

urlpatterns = [
    path('user-profile/<str:pk>/',views.UserProfile,name="user-profile"),
    path('update-profile/<str:pk>/',views.updateProfile,name="update-profile"),

    path('login/',views.loginUser,name="login"),
    path('register/',views.registerUser,name="register"),
    path('logout/',views.logoutUser,name="logout"),
]