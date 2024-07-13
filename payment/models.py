from django.db import models
from user.models import CustomUser

class Transaction(models.Model):

    TRANSACTION_TYPES_CHOICES = (
        ('d', 'deposit'),
        ('t', 'transfer')
    )

    payer = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='payer')
    payee = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='payee')
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    transaction_type = models.CharField(max_length=1, choices=TRANSACTION_TYPES_CHOICES)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Transaction carried out by {self.payer} to {self.payee}"
