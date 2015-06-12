from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from django.shortcuts import render
from random import randint

from .models import Call


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_data(self):
        def data():
            return [randint(0, 100) for x in range(7)]
        return [data() for x in range(randint(1,5))]


line_chart = TemplateView.as_view(template_name='leads/line_chart.html')
line_chart_json = LineChartJSONView.as_view()


def list_calls(request):
    calls_list = Call.objects.all()
    context = {'calls_list': calls_list}
    return render(request, 'leads/calls_audit.html', context)