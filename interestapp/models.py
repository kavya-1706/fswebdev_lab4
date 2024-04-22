


# interest/models.py
from django.db import models

class InterestCalculation(models.Model):
    principal_amount = models.FloatField()
    interest_rate = models.FloatField()
    time_period = models.IntegerField()
    interest = models.FloatField(blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
