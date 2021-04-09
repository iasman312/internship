from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


HOMEPAGE_URL = 'products/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('shop.urls')),
    path('', RedirectView.as_view(url=HOMEPAGE_URL, permanent=True))
]
