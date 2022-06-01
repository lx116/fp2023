from django.db import models


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=120)
    logo = models.CharField(max_length=500)
    red_card = models.IntegerField(default=0)
    yellow_card = models.IntegerField(default=0)
    shots_on_target = models.FloatField(default=0)
    shots = models.FloatField(default=0)
    fouls_committed = models.FloatField(default=0)
    corner = models.FloatField(default=0)
    match = models.IntegerField(default=0)

    def __str__(self):
        return self.name

