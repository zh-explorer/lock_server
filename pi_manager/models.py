from django.db import models


# Create your models here.

class Point(models.Model):
    STATUS_CHOOSE = (
        (0, "normal"),
        (1, "off line"),
        (2, "lost"),
        (3, "unknown error"),
    )

    position = models.CharField(max_length=100)
    drive_id = models.CharField(unique=True, max_length=64)
    certificate = models.CharField(max_length=10)
    status = models.IntegerField(choices=STATUS_CHOOSE)
