from rolepermissions.checkers import has_role
from user.models import CustomUser
from core.roles import Commun
from decimal import Decimal

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
