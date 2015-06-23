from django.db import models


class CallOutcome(models.Model):
    outcome = models.CharField(primary_key=True, max_length=20)
    past_tense = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return self.outcome