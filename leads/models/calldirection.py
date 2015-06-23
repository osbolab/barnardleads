from django.db import models
from . import app_label


class CallDirection(models.Model):
    class Meta:
        app_label = app_label

    direction = models.CharField(primary_key=True, max_length=20)

    def __str__(self):
        return self.direction