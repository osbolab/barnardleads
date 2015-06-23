from django.db import models


class LeadType(models.Model):
    type = models.CharField(primary_key=True, max_length=20)

    def __str__(self):
        return self.type