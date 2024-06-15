
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
""" from to_do.models import Tarea """

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(upload_to='profiles/', null=True, blank=True, default='profiles/default.jpg')
   
    def __str__(self):
        return self.user.username