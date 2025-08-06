from django.db import models

# Table: prodmast
class Product(models.Model):
    prodcode = models.CharField(max_length=20, primary_key=True)
    prodname = models.CharField(max_length=100)
    unit = models.CharField(max_length=20)
    rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.prodcode} - {self.prodname}"

# Table: stckmain
class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('IN', 'Inward'),
        ('OUT', 'Outward'),
    ]

    trno = models.CharField(max_length=20, primary_key=True)
    trdate = models.DateField()
    trtype = models.CharField(max_length=3, choices=TRANSACTION_TYPES)

    def __str__(self):
        return f"{self.trno} ({self.trtype})"

# Table: stckdetail
class StockDetail(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.transaction.trno} - {self.product.prodcode} ({self.qty})"
