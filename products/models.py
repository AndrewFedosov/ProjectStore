from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Product %s" % self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Product_image(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images of products/")
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Image %s" % self.id

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"