import json
from pathlib import Path

from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.objects.all().delete()

        filepath = Path.cwd() / 'data.json'
        with open(filepath, encoding='utf-8') as f:
            data_list = json.load(f)

        products_to_add = []
        categories_to_add = []

        for data in data_list:
            data.pop('pk', None)
            if data['model'] == 'catalog.product':
                products_to_add.append(Product(**data['fields']))
            else:
                categories_to_add.append(Category(**data['fields']))

        # print(products_to_add)
        # print(categories_to_add)

        Product.objects.bulk_create(products_to_add)
        Category.objects.bulk_create(categories_to_add)
