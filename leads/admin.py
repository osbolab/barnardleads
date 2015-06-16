from datetime import datetime, timedelta, time
from django.contrib import admin
from django.forms.models import ModelForm

from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ExportActionModelAdmin

from .models import LeadType, LeadStatus, Lead, CallDirection, CallOutcome, Call


class AlwaysChangedModelForm(ModelForm):
    def has_changed(self):
        """ Always return true to force inline form state update when default values are present."""
        return True


class CallInline(admin.TabularInline):
    model = Call
    extra = 0
    form = AlwaysChangedModelForm


class LeadAdmin(admin.ModelAdmin):
    class LastCalledListFilter(admin.SimpleListFilter):
        title = 'last called'
        parameter_name = 'last_called'

        def lookups(self, request, model_admin):
            return (
                ('Today', 'Today'),
                ('Not today', 'Not today')
            )

        def queryset(self, request, queryset):
            today = datetime.now().date()
            tomorrow = today + timedelta(1)

            if self.value() == 'Today':
                return queryset.filter(call__date__range=(today, tomorrow)).distinct()
            if self.value() == 'Not today':
                return queryset.exclude(call__date__range=(today, tomorrow))

    class DncListFilter(admin.SimpleListFilter):
        title = 'callable'
        parameter_name = 'dnc'

        def lookups(self, request, model_admin):
            return (
                (None, 'Not on DNC'),
                ('yes', 'Do not call'),
                ('all', 'All'),
            )

        def choices(self, cl):
            for lookup, title in self.lookup_choices:
                yield {
                    'selected': self.value() == lookup,
                    'query_string': cl.get_query_string({
                        self.parameter_name: lookup,
                    }, []),
                    'display': title,
                }

        def queryset(self, request, queryset):
            qvalues = {None: '0', 'yes': '1'}
            if self.value() in qvalues.keys():
                return queryset.filter(dnc__exact=qvalues[self.value()])

    list_display = ('status', 'type', 'name', 'phone1', 'phone2', 'spouse', 'notes', 'can_call', 'call_count')
    list_filter = ('status', 'type', 'created', LastCalledListFilter, DncListFilter)
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
    list_display = ('date', 'direction', 'get_name', 'get_phone1', 'get_phone2', 'outcome', 'notes')
    list_filter = ('direction', 'outcome', 'date')
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
admin.site.register([LeadType, LeadStatus, CallDirection, CallOutcome])