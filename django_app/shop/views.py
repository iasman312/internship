from django.views.generic import ListView, DetailView
from .models import Product


class IndexView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'


class ProductView(DetailView):
    model = Product
    template_name = 'product-view.html'
