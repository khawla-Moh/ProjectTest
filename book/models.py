from datetime import timezone
from django.db import models

# Create your models here.



class Book(models.Model):
    name=models.CharField(max_length="100")
    publish_date=models.DateTimeField(default=timezone.now)
    price=models.DecimalField(max_digits=8, decimal_places=2)    