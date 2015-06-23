from django.db import models


class CallDirection(models.Model):
    direction = models.CharField(primary_key=True, max_length=20)

    def __str__(self):
        return self.direction