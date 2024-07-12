from rolepermissions.roles import AbstractUserRole


class CommunPerson(AbstractUserRole):
    available_permissions = {
        'can_make_transfer': True,
        'can_receive_transfer': True
    }


class StorekeeperPerson(AbstractUserRole):
    available_permissions = {
        'can_make_transfer': False,
        'can_receive_transfer': True
    }