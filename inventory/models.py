from django.db import models


class ProductGroup(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=45)
    hierarchy = models.CharField(max_length=45)
    img_url = models.CharField(max_length=255)
    product_group = models.ForeignKey("ProductGroup", null=True, on_delete=models.SET_NULL)


class Discount(models.Model):
    status = models.CharField(max_length=45)
    turnover_class = models.CharField(max_length=45)
    product_group = models.ForeignKey("ProductGroup", on_delete=models.CASCADE)
    value = models.IntegerField()

    class Meta:
        unique_together = (("status", "turnover_class", "product_group"),)

    def __str__(self):
        return f"{self.product_group} | {self.status} | {self.turnover_class} : {self.value} %"
