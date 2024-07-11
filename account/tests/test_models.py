from django.test import TestCase
from account.models import CustomUser

class CustomUserTestCase(TestCase):
    
    def setUp(self):
        self.user_with_cpf = CustomUser.objects.create_user(
            email='usercpf@gmail.com',
            password='123',
            cpf_cnpj='333.333.333-33'
        )
        self.user_with_cpf.save()

        self.user_with_cnpj = CustomUser.objects.create_user(
            email='usercnpj@gmail.com',
            password='123',
            cpf_cnpj='22.222.222/2222-22'
        )
        self.user_with_cnpj.save()

    def test_check_user_with_cpf(self):
        user_cpf = self.user_with_cpf.cpf_cnpj
        self.assertEqual(user_cpf, '33333333333')
    
    def test_check_user_with_cnpj(self):
        user_cnpj = self.user_with_cnpj.cpf_cnpj
        self.assertEqual(user_cnpj, '22222222222222')

    def test_check_user_with_cpf_formated_cpf(self):
        formated_cpf= self.user_with_cpf.get_formated_cpf_cnpj()
        self.assertEqual(formated_cpf, '333.333.333-33')
        
    def test_check_user_with_cnpj_formated_cnpj(self):
        formated_cnpj = self.user_with_cnpj.get_formated_cpf_cnpj()
        self.assertEqual(formated_cnpj, '22.222.222/2222-22')
    
    def test_check_password_user_with_cpf(self):
        self.assertTrue(self.user_with_cpf.check_password('123'))
    def test_check_password_user_with_cnpj(self):
        self.assertTrue(self.user_with_cnpj.check_password('123'))
