from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import MinuteChanges

def index(req):
    recent_minute_changes = MinuteChanges.objects.order_by('-date')[:5]
    context = {
        'recent_minute_changes': recent_minute_changes,
    }
    return render(req, 'minute_changes/index.html', context)

def detail(req, minute_changes_id):
    change = get_object_or_404(MinuteChanges, pk=minute_changes_id)
    return render(req, 'minute_changes/detail.html', {'change': change})
