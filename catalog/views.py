from django.shortcuts import render, get_list_or_404

from catalog.models import Product


def home(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Главная'
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have a new message from {name} ({phone}) {message}')
    return render(request, 'catalog/contacts.html', context)


def product(request, pk):
    context = {
        'object_list': Product.objects.filter(pk=pk),
        }
    return render(request, 'catalog/product.html', context)
