from django.db import models

class TrainingMax(models.Model):
    squat = models.IntegerField()
    deadlift = models.IntegerField()
    bench_press = models.IntegerField()
    overhead_press = models.IntegerField()
    record_date = models.DateField()
    
    def __str__(self):
        return f'{self.squat, self.deadlift, self.bench_press, self.overhead_press, self.record_date}'
