from django.db import models

class Note(models.Model):
    NOTE_CHOICES = (
        ('A', 'A'),
        ('As', 'A#'),
        ('B', 'B'),
        ('C', 'C'),
        ('Cs', 'C#'),
    )

    note = models.CharField(max_length=2, choices=NOTE_CHOICES, default='A')

class Chord(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ChordPair(models.Model):
    chord1 = models.ForeignKey(Chord, related_name='chord1', on_delete=models.PROTECT)
    chord2 = models.ForeignKey(Chord, related_name='chord2', on_delete=models.PROTECT)

    def __str__(self):
        return "{} <-> {}".format(self.chord1, self.chord2)

class MinuteChanges(models.Model):
    duration = models.IntegerField(default=1)
    date = models.DateTimeField('Practice Time')
    chord_pair = models.ForeignKey(ChordPair, on_delete=models.PROTECT)
    changes = models.IntegerField(default=0)

    def __str__(self):
        return "{}: ({}) {} change(s) in {} minute(s)".format(
                str(self.date),
                self.chord_pair,
                self.changes,
                self.duration)

def create_chord_pairs(instance, created, raw, **kwargs):
    # not a new chord
    if not created or raw:
        return

    # get all current chords excluding the new one
    chords = Chord.objects.exclude(name=instance.name)
    if len(chords) < 1:
        # no existing chords, can't make pairs
        return

    for chord in chords:
        # create the new pairs. Order doesn't matter
        ChordPair.objects.create(chord1=instance, chord2=chord)


models.signals.post_save.connect(create_chord_pairs, sender=Chord, dispatch_uid='create_chord_pairs')
