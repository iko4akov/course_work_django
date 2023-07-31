from config.urls import path
from send.apps import SendConfig

from send.views import SendListView, SendCreateView, SendDeleteView, SendDetailView, SendUpdateView

app_name = SendConfig.name

urlpatterns = [
    path('create/', SendCreateView.as_view(), name='create'),
    path('', SendListView.as_view(), name='send_list'),
    path('detail/<int:pk>', SendDetailView.as_view(), name='view'),
    path('update/<int:pk>', SendUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', SendDeleteView.as_view(), name='delete'),
]
