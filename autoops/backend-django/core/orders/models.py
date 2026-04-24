from django.db import models


class Order(models.Model):

    order_id = models.CharField(max_length=100, unique=True)

    customer_name = models.CharField(max_length=200)

    product_name = models.CharField(max_length=200)

    weight = models.CharField(max_length=50, blank=True, null=True)

    city = models.CharField(max_length=100)

    courier = models.CharField(max_length=100, blank=True)

    status = models.CharField(
        max_length=50,
        default="pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order_id} - {self.product_name}"