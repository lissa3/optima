from django.db import models
from django.core.validators import MaxValueValidator

from clients.models import Client


class Service(models.Model):
    name = models.CharField(max_length=120)
    full_price = models.DecimalField(decimal_places=2, max_digits=6)


class Plan(models.Model):
    """ """

    PLAN_TYPES = (("F", "Full"), ("D", "Discount"), ("S", "Social"))

    plan_type = models.CharField(
        max_length=1,
        choices=PLAN_TYPES,
        default="F",
    )
    discount_percent = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(100)], default=0
    )


class Subscription(models.Model):
    client = models.ForeignKey(
        Client, on_delete=models.PROTECT, related_name="subscriptions"
    )
    service = models.ForeignKey(
        Service, on_delete=models.PROTECT, related_name="subscriptions"
    )
    plan = models.ForeignKey(
        Plan, on_delete=models.PROTECT, related_name="subscriptions"
    )
