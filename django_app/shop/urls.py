from django.urls import path
from .views import IndexView, ProductView


urlpatterns = [
    path('', IndexView.as_view(), name='product-list'),
    path('<int:pk>/', ProductView.as_view(), name='product-view'),
]