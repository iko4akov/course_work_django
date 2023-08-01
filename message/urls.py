from config.urls import path
from message.apps import MessageConfig
from message.views import MessageCreateView, MessageListView, MessageDetailView, MessageUpdateView, MessageDeleteView

app_name = MessageConfig.name

urlpatterns = [
    path('message/', MessageListView.as_view(), name='message_list'),
    path('message/detail/<int:pk>', MessageDetailView.as_view(), name='detail'),
    path('message/create/', MessageCreateView.as_view(), name='create'),
    path('message/update/<int:pk>', MessageUpdateView.as_view(), name='update'),
    path('message/delete/<int:pk>', MessageDeleteView.as_view(), name='delete'),
]
