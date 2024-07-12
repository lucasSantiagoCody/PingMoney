from rolepermissions.roles import AbstractUserRole


class Commun(AbstractUserRole):
    available_permissions = {
        'can_make_transfer': True,
        'can_receive_transfer': True
    }


class Storekeeper(AbstractUserRole):
    available_permissions = {
        'can_make_transfer': False,
        'can_receive_transfer': True
    }