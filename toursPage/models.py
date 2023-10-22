from django.db import models


class Tour(models.Model):
    tour_name = models.CharField('Tour name', max_length=255, default='Название тура')
    duration = models.IntegerField('Длительность тура', default=0)
    number_of_tourists = models.IntegerField('Количество человек в группе', default=0)
    is_available_for_children = models.BooleanField('Подходит для детей', default=True)
    price = models.IntegerField('Стоимость', default=0)

    def __str__(self):
        return self.tour_name
