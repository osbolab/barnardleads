from datetime import datetime, timedelta
from django.contrib.admin import SimpleListFilter

from import_export.resources import ModelResource
from import_export.admin import ExportActionModelAdmin

from extraadminfilters.filters import UnionFieldListFilter

from leads.models import Lead

from .calladmin import InlineCallAdmin
from .phoneformat import generify_phone_search


class LastCalledListFilter(SimpleListFilter):
    title = 'last called'
    parameter_name = 'last_called'

    def lookups(self, request, model_admin):
        return (
            ('Today', 'Today'),
            ('Not today', 'Not today'),
            ('Never', 'Never')
        )

    def queryset(self, request, queryset):
        if self.value() == 'Never':
            return queryset.filter(call=None)
        else:
            today = datetime.now().date()
            tomorrow = today + timedelta(1)
            outgoing_calls_today = {
                'call__direction__direction': 'Outgoing',
                'call__date__range': (today, tomorrow)
            }
            if self.value() == 'Not today':
                return queryset.exclude(**outgoing_calls_today)
            elif self.value() == 'Today':
                return queryset.filter(**outgoing_calls_today).distinct()


class DncListFilter(SimpleListFilter):
    title = 'callable'
    parameter_name = 'dnc'

    def lookups(self, request, model_admin):
        return (
            ('0', 'Not on DNC'),
            ('1', 'Do not call'),
        )

    def queryset(self, request, queryset):
        if self.value() in ('0', '1'):
            return queryset.filter(dnc__exact=self.value())


class CallStatusListFilter(SimpleListFilter):
    title = 'contact status'
    parameter_name = 'contact_status'

    def lookups(self, request, model_admin):
        return (
            ('not', 'Not connected'),
            ('Voicemail', 'Voicemailed'),
            ('Connected', 'Connected')
        )

    def queryset(self, request, queryset):
        if self.value() is None:
            return
        elif self.value() == 'not':
            return queryset.exclude(call__outcome='Connected')
        else:
            return queryset.filter(call__outcome=self.value()).distinct()


class LeadResource(ModelResource):
    class Meta:
        model = Lead
        fields = ('created', 'status', 'type', 'name', 'phone1', 'phone2', 'spouse', 'dnc', 'notes')
        export_order = fields


class LeadAdmin(ExportActionModelAdmin):
    class Media:
        css = {'all': ('admin/css/lead_list.css',)}

    resource_class = LeadResource

    list_display = ('status', 'type', 'name', 'phone1', 'notes', 'call_count')
    list_display_links = ('name', 'phone1',)
    list_filter = (
        ('status', UnionFieldListFilter),
        ('type', UnionFieldListFilter),
        LastCalledListFilter,
        CallStatusListFilter,
        'created',
        DncListFilter
    )
    search_fields = ('name', 'phone1', 'phone2', 'spouse', 'notes')
    inlines = (InlineCallAdmin,)

    def get_search_results(self, request, queryset, search_term):
        search_term = generify_phone_search(search_term)
        return super(LeadAdmin, self).get_search_results(request, queryset, search_term)