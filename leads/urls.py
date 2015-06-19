from django.conf.urls import url
import leads.views as views


urlpatterns = [
    # Line chart
    url(r'^line_chart$', views.line_chart,
        name='line_chart'),
    url(r'^line_chart_json$', views.line_chart_json,
        name='line_chart_json'),

    url(r'^followup/voicemails$', views.followup.voicemails),
]