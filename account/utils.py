from .models import CustomUser
from pycpfcnpj import cpfcnpj
import re

def cpf_cnpj_validator(cpf_cnpj_value):
    if cpfcnpj.validate(cpf_cnpj_value):
        return True
    return False

def email_validator(email):
    email_regex_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    if re.fullmatch(email_regex_pattern, email):
        check_email = CustomUser.objects.filter(email=email)
        if not check_email:
            return True
    return False

def full_name_validator(full_name):
    if full_name.strip() == "" and len(full_name) < 14:
        return False
    return True