from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)


class Coupon(models.Model):
    code = models.CharField(
        max_length=10,
        unique=True,
    )
    expire_from = models.DateTimeField()
    expire_to = models.DateTimeField()
    discount = models.PositiveIntegerField(validators=
                                           [MinValueValidator(0),
                                            MaxValueValidator(99)],
                                           )
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.code
