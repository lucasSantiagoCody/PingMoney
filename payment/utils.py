from rolepermissions.checkers import has_role
from user.models import CustomUser
from core.roles import Commun
from decimal import Decimal

def payer_payee_validator(payer:int, payee:int):
    check_payer = CustomUser.objects.filter(id=int(payer))
    check_payee = CustomUser.objects.filter(id=int(payer))

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
