from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_view, name='menu'),
    path('', views.cart_view, name='cart'),
    #path('', views.checkout_view, name='checkout'),
    path('add/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
]