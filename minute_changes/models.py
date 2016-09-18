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

class MinuteChanges(models.Model):
    duration = models.IntegerField(default=1)
    date = models.DateTimeField('Practice Time')
    chord1 = models.ForeignKey(Chord, related_name='chord1', on_delete=models.PROTECT)
    chord2 = models.ForeignKey(Chord, related_name='chord2', on_delete=models.PROTECT)
    changes = models.IntegerField(default=0)

    def __str__(self):
        return "{}: ({} to {}) {} change(s) in {} minute(s)".format(
                str(self.date),
                self.chord1,
                self.chord2,
                self.changes,
                self.duration)
