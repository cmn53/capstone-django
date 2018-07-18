from django.contrib.gis.db import models
from .hotel import Hotel


class Score(models.Model):
    hotel = models.OneToOneField(Hotel, on_delete=models.CASCADE, primary_key=True)
    qtr_trips = models.IntegerField()
    qtr_freq_trips = models.IntegerField()
    qtr_dest = models.IntegerField()
    qtr_dest_trips = models.IntegerField()
    half_trips = models.IntegerField()
    half_freq_trips = models.IntegerField()
    half_dest = models.IntegerField()
    half_dest_trips = models.IntegerField()

    def __str__(self):
        return ("Score: hotel %d" %self.hotel.id)
