from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_view, name='menu'),
    path('', views.cart_view, name='cart'),
]