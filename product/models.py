from django.db import models


# Create your models here.
class products():
    product_name = models.CharField(default=None, name="product_name", max_length=500)
    product_image = models.CharField(default=None, name="product_image", max_length=500)
    product_link = models.CharField(default=None, name="product_link", max_length=500)
    product_price = models.FloatField(default=0.0, name="product_price", max_length=50)

    def __init__(self, product_name, product_image, product_link, product_price):  
        self.product_name = product_name
        self.product_image = product_image
        self.product_link = product_link
        self.product_price = product_price 

    def __str__(self):
      return self.product_name