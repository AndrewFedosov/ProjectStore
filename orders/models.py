from django.db import models
from products.models import Product

class Status(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Status of order %s" % self.id

    class Meta:
        verbose_name = "Status of order"
        verbose_name_plural = "Statuses of orders"

class Order(models.Model):
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_name = models.CharField(max_length=50, blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=13, blank=True, null=True, default=None)
    statuse = models.ForeignKey(Status, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Order %s %s" % (self.id, self.statuse.name)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class Product_in_order(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_name = models.CharField(max_length=50, blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=13, blank=True, null=True, default=None)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Product %s" % self.product.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"