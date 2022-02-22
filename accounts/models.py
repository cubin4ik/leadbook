from django.db import models
from django.contrib.auth.models import AbstractUser


def user_image_path(instance, filename):
    return f"users/{instance.pk}/profile_img/{filename}"


class User(AbstractUser):
    profile_img = models.ImageField(default="users/default_profile_img.png", upload_to=user_image_path)
    widgets = models.ManyToManyField("dashboard.Widget")
