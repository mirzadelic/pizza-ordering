import uuid

from django.db import models
from django.contrib.postgres.fields import JSONField


class Order(models.Model):
    STATUS_TYPES = (
        (1, 'Ordered'),
        (2, 'In progress'),
        (3, 'Delivered'),
    )

    customer = JSONField(null=True, blank=True)
    status = models.PositiveSmallIntegerField(choices=STATUS_TYPES)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.pk


class PizzaOrder(models.Model):
    FLAVOR_TYPES = (
        (1, 'Margarita'),
        (2, 'Marinara'),
        (3, 'Salami'),
    )

    order = models.ForeignKey(
        Order, related_name='pizza', on_delete=models.CASCADE)
    flavor = models.PositiveSmallIntegerField(choices=FLAVOR_TYPES)

    def __str__(self):
        return '%s' % self.flavor

    class Meta:
        unique_together = ('order', 'flavor')


class PizzaOrderDetails(models.Model):
    SIZE_TYPES = (
        (1, 'Small'),
        (2, 'Medium'),
        (3, 'Large'),
    )
    pizza_order = models.ForeignKey(
        PizzaOrder, related_name='details', on_delete=models.CASCADE)
    size = models.PositiveSmallIntegerField(choices=SIZE_TYPES)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return '%s - %s' % (self.size, self.quantity)
