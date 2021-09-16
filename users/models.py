from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='_default.jpg',upload_to='_profile_pics_')

    def __str__(self):
        return f'{self.user.username} Profile'