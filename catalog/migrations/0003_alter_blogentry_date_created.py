# Generated by Django 4.2.5 on 2023-09-21 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_blogentry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogentry',
            name='date_created',
            field=models.DateField(blank=True, null=True, verbose_name='Дата создания'),
        ),
    ]
