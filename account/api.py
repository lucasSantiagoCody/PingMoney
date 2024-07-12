from .utils import register_user_request_validator
from rolepermissions.roles import assign_role
from .schemas import TypeUserSchema
from ninja.errors import HttpError
from ninja.router import Router
from .models import CustomUser

router = Router()

@router.post('register/', response={200: dict})
def register_user(request, data: TypeUserSchema):
    register_user_request_validator(data)

    try:
        user = CustomUser.objects.create_user(**data.user.dict())
        user.save()
        assign_role(user, data.type_user)
        return {'message': 'successfully created account'}
    except:
        raise HttpError(status_code=500, message='Internal server error')