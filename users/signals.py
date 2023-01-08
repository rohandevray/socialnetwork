from django.db.models.signals import post_delete, post_save
from .models import Profile , Follower
from django.contrib.auth.models import User



def createProfile(sender,instance,created,**kwargs):
    # IMPORTANT : when user is created a profile for it will be generated 
    if created: #created is flag (true or false for new user)
        user = instance
        profile = Profile.objects.create(
            #auto fill info in profile when a user is created
            user = user, #auto connecting the user that triggers to its profile (user after equal is instance)
            username = user.username,
            email = user.email,
            name = user.first_name
        )

def createFollower(sender,instance,created,**kwargs):
    if created:
        user = instance
        follower = Follower.objects.create(
            user = user,
            name = user.name
        )
        


post_save.connect(createProfile,sender=User) 
post_save.connect(createFollower,sender=Follower)