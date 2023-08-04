from client.apps import ClientConfig
from config.urls import path

from client.views import ClientCreateView, ClientDeleteView, ClientDetailView, ClientUpdateView, ClientListView

app_name = ClientConfig.name

urlpatterns = [
    path('client/', ClientListView.as_view(), name='client_list'),
    path('client/detail/<int:pk>', ClientDetailView.as_view(), name='client_view'),
    path('client/update/<int:pk>', ClientUpdateView.as_view(), name='update'),
    path('client/delete/<int:pk>', ClientDeleteView.as_view(), name='delete'),
    path('client/create', ClientCreateView.as_view(), name='create'),
]
