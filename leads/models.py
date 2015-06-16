from django.db import models
from django.utils import timezone
import phonenumbers


def prettify_datetime(dt):
    dt = timezone.localtime(dt)
    return str(dt.date()) + ' at ' + dt.time().strftime('%I:%M %p')

def format_phone(phone):
    if phone:
        return phonenumbers.format_number(phonenumbers.parse(phone.strip(), 'US'), phonenumbers.PhoneNumberFormat.NATIONAL)
    else:
        return ''

def format_name(name):
    return name.strip().title()

def get_local_time():
    return timezone.localtime(timezone.now())


class LeadType(models.Model):
    type = models.CharField(primary_key=True, max_length=20)

    def __str__(self):
        return self.type


class LeadStatus(models.Model):
    status = models.CharField(primary_key=True, max_length=20)

    def __str__(self):
        return self.status


class Lead(models.Model):
    name = models.CharField(max_length=200)
    phone1 = models.CharField(unique=True, max_length=20)
    phone2 = models.CharField(blank=True, max_length=20)
    spouse = models.CharField(blank=True, max_length=200)

    dnc = models.BooleanField('Do not call', default=False)
    status = models.ForeignKey(LeadStatus, default='Cold')
    type = models.ForeignKey(LeadType, default='Expired')
    notes = models.TextField(blank=True)

    created = models.DateTimeField('discovered', default=timezone.now)

    def can_call(self):
        return not self.dnc
    can_call.boolean = True
    can_call.admin_order_field = 'dnc'

    def call_count(self):
        return len(Call.objects.filter(lead=self))

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


class CallOutcome(models.Model):
    outcome = models.CharField(primary_key=True, max_length=20)
    past_tense = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return self.outcome


class CallDirection(models.Model):
    direction = models.CharField(primary_key=True, max_length=20)

    def __str__(self):
        return self.direction


class Call(models.Model):
    lead = models.ForeignKey(Lead)
    direction = models.ForeignKey(CallDirection, default='Outgoing')
    outcome = models.ForeignKey(CallOutcome, default='Missed')
    date = models.DateTimeField('placed', default=timezone.now)
    scheduled = models.DateTimeField('rescheduled to', blank=True, null=True, default=None)
    notes = models.TextField(blank=True)

    def __str__(self):
        to = str(self.lead.name)
        prefix = prettify_datetime(self.date) + ' - '

        if self.scheduled:
            return prefix + 'Call to ' + to + ' scheduled for ' + prettify_datetime(self.scheduled)
        else:
            return prefix + str(self.outcome.past_tense) + ' ' + str(self.lead.name)