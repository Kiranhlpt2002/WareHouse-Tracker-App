from django.shortcuts import render, redirect
from .models import Product, Transaction, StockDetail
from django.utils import timezone

# Home (optional)
def home_view(request):
    return render(request, 'home.html')


# 1. Add Product
def add_product(request):
    if request.method == "POST":
        prodcode = request.POST.get("prodcode")
        prodname = request.POST.get("prodname")
        unit = request.POST.get("unit")
        rate = request.POST.get("rate")

        Product.objects.create(
            prodcode=prodcode,
            prodname=prodname,
            unit=unit,
            rate=rate
        )
        return redirect('inventory')

    return render(request, 'add_product.html')


# 2. Add IN Transaction
def add_in_transaction(request):
    if request.method == "POST":
        trno = request.POST.get("trno")
        trdate = request.POST.get("trdate")
        trtype = "IN"

        Transaction.objects.create(
            trno=trno,
            trdate=trdate,
            trtype=trtype
        )
        return redirect('inventory')

    return render(request, 'INtrans.html')


# 3. Add OUT Transaction
def add_out_transaction(request):
    if request.method == "POST":
        trno = request.POST.get("trno")
        trdate = request.POST.get("trdate")
        trtype = "OUT"

        Transaction.objects.create(
            trno=trno,
            trdate=trdate,
            trtype=trtype
        )
        return redirect('inventory')

    return render(request, 'OUTtrans.html')


# 4. Add Stock Detail
def add_stock_detail(request):
    products = Product.objects.all()
    transactions = Transaction.objects.all()

    if request.method == "POST":
        trno = request.POST.get("trno")
        prodcode = request.POST.get("prodcode")
        qty = request.POST.get("qty")

        transaction = Transaction.objects.get(trno=trno)
        product = Product.objects.get(prodcode=prodcode)

        StockDetail.objects.create(
            transaction=transaction,
            product=product,
            qty=qty
        )
        return redirect('inventory')

    return render(request, 'StockDetail.html', {
        'products': products,
        'transactions': transactions
    })


# 5. Inventory View
def inventory_view(request):
    products = Product.objects.all()
    transactions = Transaction.objects.all()
    stock_details = StockDetail.objects.all()

    return render(request, 'inventory.html', {
        'products': products,
        'transactions': transactions,
        'stock_details': stock_details
    })
