from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View
from django.urls import reverse
from datetime import datetime

from chords.models import Chord

import random


def index(req):
    context = {
        'chords': Chord.objects.all()
    }
    return render(req, 'chord_recognition/index.html', context)


"""
def detail(req, minute_changes_id):
    change = get_object_or_404(MinuteChanges, pk=minute_changes_id)
    return render(req, 'minute_changes/detail.html', {'change': change})
"""


class PractiseView(View):

    EXERCISE_TYPES = ['ssr', 'cpr', 'cqr']

    def get(self, req):
        exercise_type = req.GET.get('type', None)
        if exercise_type is None:
            pass
            exercise_type = self.EXERCISE_TYPES[0]
        if exercise_type not in self.EXERCISE_TYPES:
            return render(req, 'chord_recognition/index.html', {
                'error_message': "That's not a valid exercise type"
            })

        chord_palette = [Chord.objects.get(pk=pk)
                         for pk in req.GET.getlist('chord')]

        num_chords = int(req.GET.get('num_chords', 4))

        # choose a few random chords for the exercise
        chords = [random.choice(chord_palette) for _ in range(num_chords)]

        return render(req, 'chord_recognition/practise.html', {
            'chord_palette': chord_palette,
            'chords': chords
        })

    def post(self, req):
        # return HttpResponseRedirect(reverse('minute_changes:index'))
        return HttpResponse("Chord Practise POST.")
