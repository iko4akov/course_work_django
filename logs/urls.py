from client.apps import ClientConfig
from config.urls import path

from client.views import ClientCreateView, ClientDeleteView, ClientDetailView, ClientUpdateView, ClientListView

app_name = ClientConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='client_list'),
    path('detail/<int:pk>', ClientDetailView.as_view(), name='client_view'),
    path('update/<int:pk>', ClientUpdateView.as_view(), name='client_update'),
    path('delete/<int:pk>', ClientDeleteView.as_view(), name='delete_update'),
    path('create/<int:pk>', ClientCreateView.as_view(), name='delete_update'),
]
