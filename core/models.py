from django.db import models
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
from django.conf import settings

# User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    image = models.CharField(max_length=255, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

    created_at = models.DateTimeField(auto_now_add=True)
    updates_at = models.DateTimeField(auto_now=True)
