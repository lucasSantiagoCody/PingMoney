from django.db import models
from django.contrib.auth.models import AbstractUser 
from decimal import Decimal


class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=False, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    full_name = models.CharField(max_length=50, null=False)
    cpf_cnpj = models.CharField(max_length=14, unique=True, null=False)
    amount = models.DecimalField(max_digits=9, decimal_places=2, default=Decimal('0.00'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    def save(self, *args, **kwargs):
        self.cpf_cnpj = self.cpf_cnpj.replace('.', '').replace('-', '').replace('/', '')
        super(CustomUser, self).save(*args, **kwargs)
    
    def get_formated_cpf_cnpj(self):
        # if it is cpf
        if len(self.cpf_cnpj) == 11:
            formated_cpf_cnpj = f"{self.cpf_cnpj[0:3]}.{self.cpf_cnpj[3:6]}.{self.cpf_cnpj[6:9]}-{self.cpf_cnpj[9:11]}"
            return formated_cpf_cnpj
        
        # if it is cnpj
        elif len(self.cpf_cnpj) == 14:
            
            formated_cpf_cnpj = f"{self.cpf_cnpj[0:2]}.{self.cpf_cnpj[2:5]}.{self.cpf_cnpj[5:8]}/{self.cpf_cnpj[8:12]}-{self.cpf_cnpj[12:14]}"
            return formated_cpf_cnpj
            
    def __str__(self):
        return self.full_name