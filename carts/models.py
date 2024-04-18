from django.db import models

from goods.models import Products
from users.models import User


class CartQuerryset(models.QuerySet):

    def total_price(self):
        return sum(item.product_price() for item in self)


    def total_quantity(self):
        if self:
            return sum(item.quantity for item in self)
        return 0

class Cart(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="Пользователь")
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name="Количество")
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"


    def product_price(self):
        return round(self.product.sell_price() * self.quantity, 2)


    objects = CartQuerryset().as_manager()


    def __str__(self):
        return "Корзина пользователя {} товар {} в количетсве {} (дата {})".format(self.user, self.product, self.quantity, self.created_timestamp)
