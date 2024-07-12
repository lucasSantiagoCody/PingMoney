from pycpfcnpj import cpfcnpj

def cpf_cnpj_validator(cpf_cnpj_value):
    if cpfcnpj.validate(cpf_cnpj_value):
        return True
    return False
