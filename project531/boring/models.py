from django.db import models
# Create your models here.

class BbbUser(models.Model):
    name = models.CharField(max_length=20)
    
class Tm(models.Model):
    date = models.DateField()
    user = models.ForeignKey('BbbUser', on_delete=models.CASCADE)
    
class TmData(models.Model):
    LIFTS = (
        ('Squat', 'Squat'),
        ('Deadlift', 'Deadlift'),
        ('Overhead Press', 'Overhead Press'),
        ('Bench Press', 'Bench Press')
    )
    lift = models.CharField(choices=LIFTS, max_length=10)
    weight = models.PositiveIntegerField()
    tm = models.ForeignKey('Tm', on_delete=models.CASCADE)
    

class Cycle(models.Model):
    LIFTS = (
        ('Squat', 'Squat'),
        ('Deadlift', 'Deadlift'),
        ('Overhead Press', 'Overhead Press'),
        ('Bench Press', 'Bench Press')
    )
    lift = models.CharField(choices=LIFTS, max_length=10)
    weight = models.PositiveIntegerField()
    date = models.DateField()
    cycle = models.PositiveIntegerField()
    tm = models.ForeignKey('Tm', on_delete=models.CASCADE)
