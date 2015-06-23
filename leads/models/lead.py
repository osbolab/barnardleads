from django.db import models
from django.utils import timezone
from django.template.defaultfilters import truncatechars

from leads.models.phoneformat import format_phone
from . import LeadStatus, LeadType


def format_name(name):
    return name.strip().title()

class Lead(models.Model):
    name = models.CharField(max_length=200)
    phone1 = models.CharField('phone', unique=True, max_length=20)
    phone2 = models.CharField('alt', blank=True, max_length=20)
    spouse = models.CharField(blank=True, max_length=200)

    dnc = models.BooleanField('do not call', default=False)
    status = models.ForeignKey(LeadStatus, default='Cold')
    type = models.ForeignKey(LeadType, default='Expired')
    notes = models.TextField(blank=True)

    created = models.DateTimeField('discovered', default=timezone.now)

    def can_call(self):
        return not self.dnc
    can_call.boolean = True
    can_call.admin_order_field = 'dnc'

    def call_count(self):
        from . import Call
        return len(Call.objects.filter(lead=self))
    call_count.short_description = 'calls'

    def short_name(self):
        return truncatechars(self.name, 20)
    short_name.short_description = 'name'

    def short_notes(self):
        return truncatechars(self.notes, 20)
    short_notes.short_description = 'notes'

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Lead, self).save(*args, **kwargs)

    def clean(self):
        self.name = format_name(self.name)
        self.spouse = format_name(self.spouse)
        self.phone1 = format_phone(self.phone1)
        self.phone2 = format_phone(self.phone2)

    def __str__(self):
        s = str(self.type) + ': ' + self.name + ' '
        if self.dnc:
            s += '(DNC)'
        else:
            s += self.phone1
            if self.phone2:
                s += ', ' + self.phone2
        return s