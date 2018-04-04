from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.

class User(AbstractUser):
    permisson = models.ManyToManyField(
        "pi_manager.Point",
        through='UserPermisson',
        through_fields=("user", "point")
    )


class UserPermisson(models.Model):
    PERMISSON_CHOOSE = (
        (0, 'no permisson'),
        (1, "open"),
        (2, "request open"),
        (3, "owner"),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    point = models.ForeignKey("pi_manager.Point", on_delete=models.CASCADE)
    permisson = models.IntegerField()
    time_out = models.DateTimeField()


class OpenRecord(models.Model):
    ACTION_CHOOSE = (
        (0, 'open success'),
        (1, "permisson denied"),
        (2, "open failed"),
        (3, "authorization user"),
    )

    time = models.DateTimeField(auto_now=True)
    action = models.IntegerField(choices=ACTION_CHOOSE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING)
    point = models.ForeignKey("pi_manager.Point", models.DO_NOTHING)
