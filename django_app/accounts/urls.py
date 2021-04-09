from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register_view, update_user


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', register_view, name='create'),
    path('update/', update_user, name='update-user')
]