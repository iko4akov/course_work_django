from config.urls import path
from message.apps import MessageConfig
from message.views import MessageCreateView, MessageListView, MessageDetailView, MessageUpdateView, MessageDeleteView

app_name = MessageConfig.name

urlpatterns = [
    path('', MessageListView.as_view(), name='list'),
    path('detail/<int:pk>', MessageDetailView.as_view(), name='detail'),
    path('create/', MessageCreateView.as_view(), name='create'),
    path('update/<int:pk>', MessageUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', MessageDeleteView.as_view(), name='delete'),
]
