from django.contrib import admin
from django.forms.models import ModelForm

from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ExportActionModelAdmin

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
    list_display = ('status', 'type', 'name', 'phone1', 'phone2', 'spouse', 'notes', 'can_call', 'call_count')
    list_filter = ('status', 'type', 'created', 'dnc')
    search_fields = ('name', 'phone1', 'phone2', 'spouse', 'notes')
    inlines = (CallInline,)


class CallResource(resources.ModelResource):
    lead = fields.Field(column_name='lead', attribute='lead',
                        widget=ForeignKeyWidget(Lead, 'name'))
    phone1 = fields.Field(column_name='phone1', attribute='lead',
                          widget=ForeignKeyWidget(Lead, 'phone1'))
    phone2 = fields.Field(column_name='phone2', attribute='lead',
                          widget=ForeignKeyWidget(Lead, 'phone2'))

    class Meta:
        model = Call
        fields = ('date', 'lead', 'phone1', 'phone2', 'outcome', 'notes')
        export_order = fields


class CallAdmin(ExportActionModelAdmin):
    list_display = ('date', 'get_name', 'get_phone1', 'get_phone2', 'outcome', 'notes')
    list_filter = ('outcome', 'date')
    search_fields = ('lead__name', 'lead__phone1', 'lead__phone2', 'notes',)
    resource_class = CallResource

    def get_name(self, call):
        return call.lead.name
    get_name.short_description = 'Name'
    get_name.admin_order_field = 'lead__name'

    def get_phone1(self, call):
        return call.lead.phone1
    get_phone1.short_description = 'Phone'
    get_phone1.admin_order_field = 'lead__phone1'

    def get_phone2(self, call):
        return call.lead.phone2
    get_phone2.short_description = 'Alt.'
    get_phone2.admin_order_field = 'lead__phone2'


admin.site.register(Lead, LeadAdmin)
admin.site.register(Call, CallAdmin)
admin.site.register([LeadType, LeadStatus, CallOutcome])