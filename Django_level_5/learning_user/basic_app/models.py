from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfileInfo(models.Model):
    # Create a relationship that (don't inherit from User)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add any additional attribute you want
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics", blank=True)

    # Built in attribute of django.contrib.auth.models.User
    def __str__(self):
        return self.user.username
