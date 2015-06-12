from django.contrib import admin
from django.forms.models import ModelForm

from .models import LeadType, LeadStatus, Lead, CallOutcome, Call


class AlwaysChangedModelForm(ModelForm):
    def has_changed(self):
        """ Always return true to force inline form state update when default values are present."""
        return True


class CallInline(admin.TabularInline):
    model = Call
    extra = 0
    form = AlwaysChangedModelForm


class LeadAdmin(admin.ModelAdmin):
    inlines = (CallInline,)


admin.site.register(Lead, LeadAdmin)
admin.site.register([LeadType, LeadStatus, CallOutcome, Call])