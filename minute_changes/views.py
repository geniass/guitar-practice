from django.shortcuts import render
from django.http import HttpResponse

from .models import MinuteChanges

def index(req):
    recent_minute_changes = MinuteChanges.objects.order_by('-date')[:5]
    output = '\n'.join(recent_minute_changes)
    return HttpResponse(output)

def detail(req, minute_changes_id):
    return HttpResponse('changes: %s' % minute_changes_id)
