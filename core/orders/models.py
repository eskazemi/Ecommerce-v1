from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product


class Order(models.Model):
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.PROTECT,
                             related_name="orders",
                             )
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_order_price(self):
        return sum(item.get_cost() for item in self.items.all())

    class Meta:
        ordering = ('paid', '-updated_at')

    def __str__(self):
        return f'{self.user} - {self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        return self.price * self.quantity
