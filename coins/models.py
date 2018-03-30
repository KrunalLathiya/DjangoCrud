from django.db import models

class Coin(models.Model):
    coin_name = models.CharField(max_length=30)
    coin_price = models.IntegerField()
    created_at = models.DateField()
    def __str__(self):
        return self.coin_name