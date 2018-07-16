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

    @property
    def weekly_trips(self):
        # Total trips operated on pattern during an average week
        total = (self.wk_trips * 5) + self.sa_trips + self.su_trips
        return total

    @property
    def early_am_trips(self):
        # Total weekday trips operated on pattern from 3AM-6AM
        total = self.wk_03_06
        return total

    @property
    def core_hour_trips(self):
        # Total weekday trips operated on pattern from 6AM-6PM
        total = self.wk_06_09 + self.wk_09_12 + self.wk_12_15 + self.wk_15_18
        return total

    @property
    def evening_trips(self):
        # Total weekday trips operated on pattern from 6PM-9PM
        total = self.wk_18_21
        return total

    @property
    def night_trips(self):
        # Total weekday trips operated on pattern from 9PM-3AM
        total = self.wk_21_24 + self.wk_24_28 + self.wk_00_03
        return total
