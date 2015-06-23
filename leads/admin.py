from datetime import datetime, timedelta
from django.contrib import admin
from django.forms.models import ModelForm
from django.core.urlresolvers import reverse

from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ExportActionModelAdmin

import phonenumbers

from extraadminfilters.filters import UnionFieldListFilter

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
    class Media:
        css = {'all': ('admin/css/lead_list.css',)}

    class LastCalledListFilter(admin.SimpleListFilter):
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

    class DncListFilter(admin.SimpleListFilter):
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

    class CallStatusListFilter(admin.SimpleListFilter):
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
    inlines = (CallInline,)

    def get_search_results(self, request, queryset, search_term):
        try:
            phone_number = phonenumbers.parse(search_term.strip(), 'US')
            if phonenumbers.is_possible_number(phone_number):
                search_term = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.NATIONAL)
        except phonenumbers.NumberParseException:
            pass

        return super(LeadAdmin, self).get_search_results(request, queryset, search_term)


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
    class Media:
        css = {'all': ('admin/css/call_list.css',)}

    list_display = ('format_date', 'direction', 'get_name', 'get_phone1', 'outcome', 'notes')
    list_filter = (
        ('direction', UnionFieldListFilter),
        ('outcome', UnionFieldListFilter),
        'date'
    )
    search_fields = ('lead__name', 'lead__phone1', 'lead__phone2', 'notes',)
    resource_class = CallResource

    def format_date(self, call):
        return call.date.strftime('%x')
    format_date.short_description = 'placed'
    format_date.admin_order_field = 'date'

    def get_name(self, call):
        return call.lead.name
    get_name.short_description = 'name'
    get_name.admin_order_field = 'lead__name'

    def get_phone1(self, call):
        return call.lead.phone1
    get_phone1.short_description = 'phone'
    get_phone1.admin_order_field = 'lead__phone1'


admin.site.register(Lead, LeadAdmin)
admin.site.register(Call, CallAdmin)
admin.site.register([LeadType, LeadStatus, CallDirection, CallOutcome])