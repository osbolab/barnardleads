app_label = 'leads'

from .leadstatus import LeadStatus
from .leadtype import LeadType
from .lead import Lead

from .calldirection import CallDirection
from .calloutcome import CallOutcome
from .call import Call


__all__ = ['LeadStatus', 'LeadType', 'Lead',
           'CallDirection', 'CallOutcome', 'Call']