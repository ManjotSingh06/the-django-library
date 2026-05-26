from django.db import models
from django.contrib.auth.models import User

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    image = models.ImageField(default='default_profile.jpg', upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return self.user.username
