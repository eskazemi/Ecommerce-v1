from django.db import models
from django.contrib.auth import get_user_model


class Order(models.Model):
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.PROTECT,
                             related_name="orders",
                             )
    paid = models.BooleanField(default=False)
    discount = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_order_price(self):
        total = sum(item.get_cost() for item in self.items.all())
        if self.discount:
            discount_price = (self.discount / 100) * total
            return int(total - discount_price)
        else:
            return total
    class Meta:
        ordering = ('paid', '-updated_at')

    def __str__(self):
        return f'{self.user} - {self.id}'
