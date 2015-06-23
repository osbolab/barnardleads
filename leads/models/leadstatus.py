from django.db import models


class LeadStatus(models.Model):
    status = models.CharField(primary_key=True, max_length=20)

    def __str__(self):
        return self.status