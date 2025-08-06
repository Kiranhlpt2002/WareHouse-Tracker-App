from django.contrib import admin
from .models import Product, Transaction, StockDetail

admin.site.register(Product)
admin.site.register(Transaction)
admin.site.register(StockDetail)
