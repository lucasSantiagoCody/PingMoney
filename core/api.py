from ninja import NinjaAPI
from account.api import router as account_router

api = NinjaAPI()

api.add_router('account/', account_router)