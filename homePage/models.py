from django.db import models


class Employer(models.Model):
    name = models.CharField('User name', max_length=30)
    e_mail = models.EmailField('e-mail address', max_length=255)
    organization = models.TextField('Organization', max_length=1000)

    def __str__(self):
        return self.name
