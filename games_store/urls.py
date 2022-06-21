from django.contrib import admin
from django.urls import path
from .api import api 
# from games_store.core.api import router_api

# api = NinjaAPI(
#     version='1.0',
#     title='Game Store API',
#     description='CRUD - Create, Retrieve, Update, Delete are the four basic functions of persistent storage.\n'
#                 'https://github.com/liviocunha/django-ninja-crud',
#     urls_namespace='public_api',
# )

# api.add_router('/v1/', router_api)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', api.urls),
]
