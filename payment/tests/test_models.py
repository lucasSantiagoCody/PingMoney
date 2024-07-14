from django.test import TestCase
from payment.models import Transaction
from user.models import CustomUser
from decimal import Decimal

class TransactionTestCase(TestCase):
    
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            full_name='testuser',
            email='testuser@gmail.com',
            password='testuser123',
        )
        self.transaction = Transaction.objects.create(
            payer=self.user,
            payee=self.user,
            amount=Decimal(2000.99),
            transaction_type='d'
        )

    
    def test_check_payer(self):
        self.assertEqual(self.transaction.payer.id, self.user.id)
    
    def test_check_payee(self):
        self.assertEqual(self.transaction.payee.id, self.user.id)
    
    def test_check_amount(self):
        self.assertIsInstance(self.transaction.amount, Decimal)

    def test_check_transaction_type(self):
        self.assertEqual(self.transaction.transaction_type, 'd')

    def test_check_get_transaction_type_property(self):
        self.assertEqual(self.transaction.get_transaction_type, 'deposit')
    










