from django.forms.models import ModelForm
from django.contrib.admin import TabularInline

from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ExportActionModelAdmin

from extraadminfilters.filters import UnionFieldListFilter

from leads.models import Call, Lead

from .phoneformat import generify_phone_search


class AlwaysChangedModelForm(ModelForm):
    def has_changed(self):
        """ Always return true to force inline form state update when default values are present."""
        return True


class InlineCallAdmin(TabularInline):
    model = Call
    extra = 0
    form = AlwaysChangedModelForm


class CallResource(resources.ModelResource):
    class Meta:
        model = Call
        fields = ('date', 'lead', 'phone1', 'phone2', 'outcome', 'notes')
        export_order = fields

    lead = fields.Field(column_name='lead', attribute='lead',
                        widget=ForeignKeyWidget(Lead, 'name'))
    phone1 = fields.Field(column_name='phone1', attribute='lead',
                          widget=ForeignKeyWidget(Lead, 'phone1'))
    phone2 = fields.Field(column_name='phone2', attribute='lead',
                          widget=ForeignKeyWidget(Lead, 'phone2'))


class CallAdmin(ExportActionModelAdmin):
    class Media:
        css = {'all': ('admin/css/call_list.css',)}

    resource_class = CallResource

    list_display = ('format_date', 'direction', 'get_name', 'get_phone1', 'outcome', 'notes')
    list_filter = (
        ('direction', UnionFieldListFilter),
        ('outcome', UnionFieldListFilter),
        'date'
    )
    search_fields = ('lead__name', 'lead__phone1', 'lead__phone2', 'notes',)

    def get_search_results(self, request, queryset, search_term):
        search_term = generify_phone_search(search_term)
        return super(CallAdmin, self).get_search_results(request, queryset, search_term)

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