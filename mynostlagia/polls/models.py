from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    custom_html = models.TextField(blank=True, null=True)  # <-- DODANE POLE na HTML/CSS użytkownika

    def __str__(self):
        return self.user.username
