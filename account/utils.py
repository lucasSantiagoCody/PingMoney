from .models import CustomUser
from pycpfcnpj import cpfcnpj
from ninja.errors import HttpError
import re


def register_user_request_validator(request_data):

    check_cpf_cnpj = cpf_cnpj_validator(request_data.user.cpf_cnpj)
    check_email = email_validator(request_data.user.email)
    check_full_name = full_name_validator(request_data.user.full_name)
    check_password = password_validator(request_data.user.password)
    check_type_user = type_user_validator(request_data.type_user)
    
    messages_error = []

    if not check_cpf_cnpj:
        messages_error.append('Invalid cpf/cnpj')
    if not check_email:
        messages_error.append('Invalid E-mail')
    if not check_full_name:
        messages_error.append('Invalid full_name')
    if not check_type_user:
        messages_error.append('Invalid type_user. Types user allowed are (commun, storekeeper)')
    if not check_password:
        messages_error.append('Invalid password min 6 characters')

    single_msg = error_message_handler(messages_error)

    if single_msg:
        raise HttpError(status_code=400, message=single_msg)

    return True
    

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
    if full_name.strip() != "" and len(full_name) >= 14:
        return True
    return False

def password_validator(pswd):
    if pswd and len(pswd) >= 6:
        return True
    return False

def type_user_validator(type_user):
    types_user_allowed = ['commun', 'storekeeper']

    if type_user and type_user in types_user_allowed:
        return True
    return False


def error_message_handler(messages_error):
    single_message = ""

    for i, msg_error in enumerate(messages_error):
        single_message += f'{msg_error}, '

    single_message = single_message.strip()
    # to dont display the last comma
    single_message = single_message[:len(single_message)-1]

    return single_message





