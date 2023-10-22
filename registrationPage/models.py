from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    e_mail = models.EmailField(max_length=300)
    isIndividual = models.BooleanField(default=False)
    company = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name
