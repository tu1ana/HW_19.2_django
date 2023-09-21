from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    photo = models.ImageField(upload_to='products/', **NULLABLE, verbose_name='Изображение(превью)')
    category = models.CharField(max_length=100, verbose_name='Категория')
    price = models.FloatField(verbose_name='Цена')
    date_created = models.DateField(verbose_name='Дата создания')
    date_last_modified = models.DateField(verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class BlogEntry(models.Model):
    heading = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', null=True, blank=True)
    content = models.TextField(verbose_name='Содержимое')
    image = models.ImageField(upload_to='blog/', ** NULLABLE, verbose_name='Изображение(превью)')
    date_created = models.DateField(** NULLABLE, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = 'запись блога'
        verbose_name_plural = 'записи блога'
