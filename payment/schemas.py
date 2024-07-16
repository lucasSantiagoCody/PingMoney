from ninja import Schema, ModelSchema
from .models import Transaction
from decimal import Decimal

class TransferSchema(Schema):
    amount: Decimal
    payer: int
    payee: int

class DepositSchema(Schema):
    depositor: int
    amount: Decimal