from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('add-product/', views.add_product, name='add_product'),
    path('add-in/', views.add_in_transaction, name='add_in_transaction'),
    path('add-out/', views.add_out_transaction, name='add_out_transaction'),
    path('add-stock-detail/', views.add_stock_detail, name='add_stock_detail'),
    path('inventory/', views.inventory_view, name='inventory'),
]
