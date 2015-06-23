from django.contrib.admin import site

from .leadadmin import LeadAdmin
from .calladmin import CallAdmin

from leads.models import LeadType, LeadStatus, Lead, CallDirection, CallOutcome, Call


site.register(Lead, LeadAdmin)
site.register(Call, CallAdmin)
site.register([LeadType, LeadStatus, CallDirection, CallOutcome])