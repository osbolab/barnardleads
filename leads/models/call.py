from django.db import models
from django.utils import timezone

from . import CallDirection, CallOutcome, Lead


def prettify_datetime(dt):
        dt = timezone.localtime(dt)
        return str(dt.date()) + ' at ' + dt.time().strftime('%I:%M %p')

class Call(models.Model):
    lead = models.ForeignKey(Lead)
    direction = models.ForeignKey(CallDirection, db_index=True, default='Outgoing', verbose_name='^/v')
    outcome = models.ForeignKey(CallOutcome, db_index=True, default='Missed')
    date = models.DateTimeField('placed', db_index=True, default=timezone.now)
    scheduled = models.DateTimeField('rescheduled to', db_index=True, blank=True, null=True, default=None)
    notes = models.TextField(blank=True)

    def __str__(self):
        to = str(self.lead.name)
        prefix = prettify_datetime(self.date) + ' - '

        if self.scheduled:
            return prefix + 'Call to ' + to + ' scheduled for ' + prettify_datetime(self.scheduled)
        else:
            return prefix + str(self.outcome.past_tense) + ' ' + str(self.lead.name)