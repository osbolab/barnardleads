from django.db import models

from . import app_label


class CallOutcome(models.Model):
    class Meta:
        app_label = app_label

    outcome = models.CharField(primary_key=True, max_length=20)
    past_tense = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return self.outcome