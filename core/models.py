from django.db import models
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
from django.conf import settings

# User = get_user_model()


class CommonInfo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=False, on_delete=models.SET_NULL)

    created_at = models.DateTimeField(auto_now_add=True)
    updates_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = []


class Post(CommonInfo):
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    image = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.title}   {self.user}"


class Like(CommonInfo):
    post = models.ForeignKey("Post", null=False, blank=False, on_delete=models.CASCADE)
    status = models.BooleanField(null=True, blank=True, default=None)


