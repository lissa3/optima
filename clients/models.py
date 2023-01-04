from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=120, default="")

    def __str__(self) -> str:
        return self.name
