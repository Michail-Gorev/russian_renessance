from django.db import models


class Employer(models.Model):
    name = models.CharField('', max_length=30)
    e_mail = models.EmailField('', max_length=255)
    organization = models.TextField('', max_length=1000)

    def __str__(self):
        return self.name
