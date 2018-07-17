from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from .metro import Metro
from .stop import Stop
from .pattern import Pattern

class Destination(models.Model):
    metro = models.ForeignKey(Metro, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    geom = models.PointField(spatial_index=True)

    def __str__(self):
        return self.name

    def nearby_stops(self):
        radius = 0.25 # miles
        stops = Stop.objects.filter(geom__distance_lte=(self.geom, Distance(mi=radius)))
        return stops

    def nearby_patterns(self):
        stops = self.nearby_stops()
        patterns = Pattern.objects.filter(stops__in=stops).distinct()
        return patterns
