from django.test import TestCase
from account.models import CustomUser

class CustomUserTestCase(TestCase):
    
    def setUp(self):
        self.user_with_cpf = CustomUser(
            email='usercpf@gmail.com',
            full_name='testfullname',
            cpf_cnpj='333.333.333-33',
            password='123'
        )
        self.user_with_cpf.save()

        self.user_with_cnpj = CustomUser(
            email='usercnpj@gmail.com',
            full_name='testfullname',
            cpf_cnpj='22.222.222/2222-22',
            password='123'
        )
        self.user_with_cnpj.save()

    def test_check_user_with_cpf_cpf(self):
        user_cpf = self.user_with_cpf.cpf_cnpj
        self.assertEqual(user_cpf, '33333333333')
    
    def test_check_user_with_cnpj_cnpj(self):
        user_cnpj = self.user_with_cnpj.cpf_cnpj
        self.assertEqual(user_cnpj, '22222222222222')

    def test_check_user_with_cpf_formated_cpf(self):
        formated_cpf= self.user_with_cpf.get_formated_cpf_cnpj()
        self.assertEqual(formated_cpf, '333.333.333-33')
        
    def test_check_user_with_cnpj_formated_cnpj(self):
        formated_cnpj = self.user_with_cnpj.get_formated_cpf_cnpj()
        self.assertEqual(formated_cnpj, '22.222.222/2222-22')
    
    