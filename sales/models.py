from django.db import models

# Create your models here.

class Sales(models.Model):
    order_id = models.CharField(max_length=50)
    order_date = models.DateField(auto_now=False, auto_now_add=False)
    ship_date = models.DateField(auto_now=False, auto_now_add=False)
    ship_mode = models.CharField(max_length=50)
    customer_id = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    segment = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    product_id = models.CharField(max_length=50)

    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    product_name = models.CharField(max_length=500)
    sales = models.FloatField()

    def __str__(self):
        return self.order_id
    