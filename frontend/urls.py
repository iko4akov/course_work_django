from config.urls import path
from frontend.apps import FrontendConfig
from frontend.views import index_view

app_name = FrontendConfig.name

urlpatterns = [
    path('', index_view, name='index_view')
]
