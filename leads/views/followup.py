from django.shortcuts import render

from leads.models import Call


def voicemails(request):
    calls_list = Call.objects.filter(outcome='Voicemail')
    context = {'calls_list': calls_list}
    return render(request, 'leads/calls_audit.html', context)