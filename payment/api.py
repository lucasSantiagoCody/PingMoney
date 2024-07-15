from .utils import transfer_request_validator
from .schemas import TransferSchema
from ninja.errors import HttpError
from user.models import CustomUser
from ninja.router import Router
from .models import Transaction
import requests

router = Router()

@router.post('transfer/', response={200: dict, 401: dict, 500: dict})
def transfer(request, request_data:TransferSchema):

    # # if there is any inconsistency in the request it will return HttpError 400
    transfer_request_validator(request_data)

    payer = CustomUser.objects.get(id=request_data.payer)
    payee = CustomUser.objects.get(id=request_data.payee)
    amount_to_transfer = request_data.value

    AUTHORIZER_ENDPOINT = "https://util.devi.tools/api/v2/authorize"

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