from core.utils import error_message_handler
from rolepermissions.checkers import has_role
from user.models import CustomUser
from ninja.errors import HttpError
from core.roles import Commun
from decimal import Decimal

def transfer_request_validator(request_data):
    check_payer_payee = payer_payee_validator(
            request_data.payer, 
            request_data.payee
            )
    payer_has_permission = check_payer_has_permission(request_data.payer)
    payer_equal_to_payee = check_payer_equal_to_payee(request_data.payer, request_data.payee)
    check_amount = amount_validator(request_data.value)
    
    messages_error = []

    if not check_payer_payee:
        messages_error.append("Payer or Payee isn't registered")
    if not check_amount:
        messages_error.append('Amount must be Decimal')
    
    if payer_has_permission == False:
        messages_error.append("Storekeepers can't make transfer")
    if payer_equal_to_payee:
        messages_error.append("Can't transfer to yourself, make a deposit")

    single_message_error = error_message_handler(messages_error)

    if single_message_error:
        raise HttpError(status_code=400, message=single_message_error)
    return True

def payer_payee_validator(payer:int, payee:int):
    check_payer = CustomUser.objects.filter(id=int(payer))
    check_payee = CustomUser.objects.filter(id=int(payee))

    if check_payer and check_payee:
        return True
    return False
      
def amount_validator(amount):
    if isinstance(amount, Decimal):
        return True
    return False

def check_payer_has_permission(payer_id):
    """ 
        if return False
            - Payer doesn't has permission
        if return None
            - User isn't registerd
    """

    try:
        payer = CustomUser.objects.get(id=payer_id)
    except:
        return None
    
    has_permission = has_role(payer, Commun)
    if not has_permission:
       return False

def check_payer_equal_to_payee(payer, payee):
    if payer == payee:
        return True
    return None

def check_payer_has_balance_to_transfer(payer_id, amount_to_transfer):

    try:
        payer_balance = CustomUser.objects.get(id=payer_id).balance
        if amount_to_transfer < payer_balance:
            return True
        else:
            return False
    except:
        raise HttpError(status_code=400, message="Payer isn't regitered")
