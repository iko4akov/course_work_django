from client.apps import ClientConfig
from config.urls import path

from client.views import ClientCreateView, ClientDeleteView, ClientDetailView, ClientUpdateView, ClientListView

app_name = ClientConfig.name

urlpatterns = [
    path('client/', ClientListView.as_view(), name='list'),
    path('detail/<int:pk>', ClientDetailView.as_view(), name='detail'),
    path('update/<int:pk>', ClientUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ClientDeleteView.as_view(), name='delete'),
    path('create/', ClientCreateView.as_view(), name='create'),
]
