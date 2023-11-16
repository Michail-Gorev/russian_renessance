from django.db import models
from django.urls import reverse



class Tour(models.Model):
    tour_id = models.IntegerField('ID тура', default=0)
    tour_name = models.CharField('Tour name', max_length=255, default='Название тура')
    duration = models.IntegerField('Длительность тура', default=0)
    number_of_tourists = models.IntegerField('Количество человек в группе', default=0)
    is_available_for_children = models.BooleanField('Подходит для детей', default=True)
    price = models.IntegerField('Стоимость', default=0)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.tour_name


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})


class TourDetail(models.Model):
    tour_id = models.IntegerField('ID тура', default=0)
    tour_name = models.CharField('Tour name', max_length=255, default='Название тура')
    duration = models.IntegerField('Длительность тура', default=0)
    number_of_tourists = models.IntegerField('Количество человек в группе', default=0)
    is_available_for_children = models.BooleanField('Подходит для детей', default=True)
    price = models.IntegerField('Стоимость', default=0)
    description = models.TextField(default='Описание тура')

    def __str__(self):
        return self.tour_name


class Visual(models.Model):
    class Meta:
        db_table = 'app_ideator_visuals'

    img = models.ImageField(upload_to='media/images', verbose_name='Файл картинки')
    title = models.CharField(max_length=120, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Описание')
    alt = models.TextField(verbose_name='Подсказка')
    index = models.IntegerField(verbose_name='Индекс')

    def __unicode__(self):
        return self.title
