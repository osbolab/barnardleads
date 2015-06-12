from django.conf.urls import url
from . import views


urlpatterns = [
    # Line chart
    url(r'^$', views.line_chart,
        name='line_chart'),
    url(r'^line_chart_json$', views.line_chart_json,
        name='line_chart_json'),

    url(r'^calls$', views.list_calls),
]