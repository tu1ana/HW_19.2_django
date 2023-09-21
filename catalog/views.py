from django.shortcuts import render, get_list_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.models import Product, BlogEntry


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Главная'
    }


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


class ProductDetailView(DetailView):
    model = Product


class BlogEntryCreateView(CreateView):
    model = BlogEntry
    fields = ('heading', 'content',)
    success_url = reverse_lazy('catalog:blogentry_list')

    def form_valid(self, form):
        if form.is_valid():
            new_entry = form.save()
            new_entry.slug = slugify(new_entry.heading)
            new_entry.save()

        return super().form_valid(form)


class BlogEntryListView(ListView):
    model = BlogEntry

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogEntryUpdateView(UpdateView):
    model = BlogEntry
    fields = ('heading', 'content',)
    # success_url = reverse_lazy('catalog:blogentry_list')

    def form_valid(self, form):
        if form.is_valid():
            new_entry = form.save()
            new_entry.slug = slugify(new_entry.heading)
            new_entry.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:view_blog', args=[self.kwargs.get('pk')])


class BlogEntryDetailView(DetailView):
    model = BlogEntry

    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        object.views_count += 1
        object.save()
        return object


class BlogEntryDeleteView(DeleteView):
    model = BlogEntry
    success_url = reverse_lazy('catalog:blogentry_list')
