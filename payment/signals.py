from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Transaction
import requests


@receiver(post_save, sender=Transaction)
def send_notify_to_payee(instance, created, **kwargs):
    if created:

        payer = instance.payer
        payee = instance.payee

        SEND_NOTIFY_ENDPOINT = "https://util.devi.tools/api/v1/notify/"

        email_message = f"{payer} just transferred {instance.amount} KZs to you"
        data = {'recipient': {'email': payee.email}, 'message':email_message}

        # simulating email sending
        requests.post(url=SEND_NOTIFY_ENDPOINT, data=data)