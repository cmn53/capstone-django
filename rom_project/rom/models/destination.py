from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from .metro import Metro

class Destination(models.Model):
    metro = models.ForeignKey(Metro, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    geom = models.PointField(spatial_index=True)

    def __str__(self):
        return self.name
