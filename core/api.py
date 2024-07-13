from ninja import NinjaAPI
from user.api import router as users_router
from payment.api import router as payments_router


api = NinjaAPI()

api.add_router('user/', users_router)
api.add_router('payment/', payments_router)