from ninja.main import NinjaAPI
from  games_store.core.api import router_api as games_router

api = NinjaAPI()
api.add_router('homologation/', games_router)