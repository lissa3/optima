import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    username = models.CharField(default="", blank=True, max_length=120)
    email = models.EmailField(unique=True, max_length=120)
    info = models.CharField(max_length=256, blank=True, default="")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self) -> str:
        return self.email
