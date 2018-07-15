from django.contrib.gis.db import models
from .route import Route
from .stop import Stop

class Pattern(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    pattern_onestop_id = models.CharField(max_length=100)
    wk_trips = models.IntegerField()
    sa_trips = models.IntegerField()
    su_trips = models.IntegerField()
    wk_00_03 = models.IntegerField()
    wk_03_06 = models.IntegerField()
    wk_06_09 = models.IntegerField()
    wk_09_12 = models.IntegerField()
    wk_12_15 = models.IntegerField()
    wk_15_18 = models.IntegerField()
    wk_18_21 = models.IntegerField()
    wk_21_24 = models.IntegerField()
    wk_24_28 = models.IntegerField()
    stops = models.ManyToManyField(Stop)

    def __str__(self):
        return "%s Pattern %s" %(self.route.operator.name, self.pattern_onestop_id)
