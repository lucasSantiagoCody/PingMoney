from rolepermissions.checkers import has_role, has_permission
from rolepermissions.roles import assign_role, clear_roles
from core.roles import Commun, Storekeeper
from user.models import CustomUser
from django.test import TestCase


class RolesTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            full_name='jhon doe',
            email='doe@gmail.com',
            password='jhondoe123'
        )

    def test_check_commun_permissions(self):
        role = Commun
        self.assertTrue(role.available_permissions['can_make_transfer'])
        self.assertTrue(role.available_permissions['can_make_deposit'])
        self.assertTrue(role.available_permissions['can_receive_transfer'])
    
    def test_check_storekeeper_permissions(self):
        role = Storekeeper
        self.assertTrue(role.available_permissions['can_make_deposit'])
        self.assertTrue(role.available_permissions['can_receive_transfer'])
        self.assertFalse(role.available_permissions['can_make_transfer'])
    
    def test_check_assignment_commun_role(self):
        assign_role(self.user, Commun)
        self.assertTrue(has_role(self.user, Commun))
    
    def test_check_assignment_storekeeper_role(self):
        assign_role(self.user, Storekeeper)
        self.assertTrue(has_role(self.user, Storekeeper))
        