from .utils import transfer_request_validator, deposit_request_validator
from .schemas import TransferSchema, DepositSchema
from ninja.errors import HttpError
from user.models import CustomUser
from ninja.router import Router
from .models import Transaction
import requests

router = Router()

AUTHORIZER_ENDPOINT = "https://util.devi.tools/api/v2/authorize"

@router.post('transfer/', response={200: dict, 401: dict, 500: dict})
def transfer(request, request_data:TransferSchema):

    # # if there is any inconsistency in the request it will return HttpError 400
    transfer_request_validator(request_data)

    payer = CustomUser.objects.get(id=request_data.payer)
    payee = CustomUser.objects.get(id=request_data.payee)
    amount_to_transfer = request_data.value

    authorizer_response = (requests.get(url=AUTHORIZER_ENDPOINT)).json()

    def transaction_fail():
        raise HttpError(status_code=500, message='Transfer fail, try again')
    
    if authorizer_response['data']['authorization'] == True:

        try:
            payer.pay(amount_to_transfer)
            payer.save()
        except:
            payer.balance += amount_to_transfer
            payer.save()
            transaction_fail()

        try:
            payee.receive(amount_to_transfer)
            payee.save()
        except:
            payee.balance -= amount_to_transfer
            payee.save()
            transaction_fail()

        try:
            transaction = Transaction(
                payer=payer,
                payee=payee,
                amount=request_data.value,
                transaction_type='t'
            )
            transaction.save()
        except:
            transaction_fail()
        return {'message': 'transfer done successfully'}
    else:
        raise HttpError(status_code=401, message='Unauthorized transfer')

@router.post('deposit/', response={200: dict})
def deposit(request, request_data:DepositSchema):

    deposit_request_validator(request_data)

    depositor_id = request_data.depositor
    amount = request_data.amount
    depositor = CustomUser.objects.get(id=depositor_id)

    def deposit_fail():
        raise HttpError(status_code=500, message='Deposit fail, try again')

    authorizer_response = (requests.get(url=AUTHORIZER_ENDPOINT)).json()

    if authorizer_response['data']['authorization'] == True:
        try:
            depositor.receive(amount)
            depositor.save()
            return {'message': 'Deposit done successfully'}
        except:
            deposit_fail()
        try:
            transaction = Transaction(
                payer=depositor,
                payee=depositor,
                amount=amount,
                transaction_type='d'
            )
            transaction.save()
        except:
            deposit_fail()
    else:
        raise HttpError(status_code=401, message='Unauthorized transfer')
