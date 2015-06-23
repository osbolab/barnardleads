from datetime import datetime, timedelta
from django.contrib.admin import ModelAdmin, SimpleListFilter

from extraadminfilters.filters import UnionFieldListFilter

from .calladmin import InlineCallAdmin
from .phoneformat import generify_phone_search


class LeadAdmin(ModelAdmin):
    class Media:
        css = {'all': ('admin/css/lead_list.css',)}

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
            today = datetime.now().date()
            tomorrow = today + timedelta(1)

            if self.value() == 'Not today':
                return queryset.exclude(call__date__range=(today, tomorrow))
            elif self.value() == 'Today':
                return queryset.filter(call__date__range=(today, tomorrow)).distinct()
            elif self.value() == 'Never':
                return queryset.filter(call=None)

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