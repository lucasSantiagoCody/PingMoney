from rolepermissions.roles import AbstractUserRole


class Commun(AbstractUserRole):
    available_permissions = {
        'can_make_transfer': True,
        'can_make_deposit': True,
        'can_receive_transfer': True
    }


class Storekeeper(AbstractUserRole):
    available_permissions = {
        'can_make_transfer': False,
        'can_make_deposit': True,
        'can_receive_transfer': True
    }