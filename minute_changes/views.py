from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View
from django.urls import reverse
from datetime import datetime
import sys

from django.db.models import Max
from .models import MinuteChanges, ChordPair

def index(req):
    recent_minute_changes = MinuteChanges.objects.order_by('-date')[:5]
    # sort the chord pairs by the maximum number of changes performed for each
    # pair, so that the worst ones appear at the top
    worst_chord_pairs = ChordPair.objects.annotate(max_changes=Max('minutechanges__changes')).order_by('max_changes')
    context = {
        'recent_minute_changes': recent_minute_changes,
        'chord_pairs': worst_chord_pairs
    }
    return render(req, 'minute_changes/index.html', context)

def detail(req, minute_changes_id):
    change = get_object_or_404(MinuteChanges, pk=minute_changes_id)
    return render(req, 'minute_changes/detail.html', {'change': change})

class PractiseView(View):
    def get(self, req, chord_pair_id):
        chord_pair = get_object_or_404(ChordPair, pk=chord_pair_id)
        return render(req, 'minute_changes/practise.html', {'chord_pair': chord_pair})

    def post(self, req, chord_pair_id):
        try:
            chord_pair = ChordPair.objects.get(pk=chord_pair_id)
        except (ValueError, KeyError, ChordPair.DoesNotExist):
            return render(req, 'minute_changes/practise.html', {'chord_pair': chord_pair, 'error_message': "Not a valid chord pair"})
            #return HttpResponseRedirect(reverse('minute_changes:index', args={'error_message': "Not a valid chord pair"}))
        change = MinuteChanges.objects.create(date=datetime.now(), chord_pair=chord_pair, changes=req.POST['changes'])
        return HttpResponseRedirect(reverse('minute_changes:index'))
