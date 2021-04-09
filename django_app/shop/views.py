from django.views.generic import ListView
from .models import Product


class IndexView(ListView):
    template_name = 'products/index.html'
    model = Product
    context_object_name = 'products'
