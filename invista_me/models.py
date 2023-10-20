from django.db import models
from datetime import datetime

# Create your models here.


class investimentos(models.Model):
    investimento = models.TextField(max_length=255)
    valor = models.FloatField()
    pago = models.BooleanField()
    data = models.DateTimeField(default=datetime.now)
    