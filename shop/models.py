from django.db import models

# Create your models here.
class phones(models.Model):
        titles = models.CharField(max_length=150)
        images = models.CharField(max_length=1000)
        prices = models.CharField(max_length=150)
        #discounts = models.CharField(max_length=150)
        class Meta:
            verbose_name = "Shopify mobiles"