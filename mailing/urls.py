from config.urls import path
from mailing.apps import MailingConfig
from mailing.views import MailingListView, MailingCreateView, MailingDeleteView, MailingDetailView, \
    MailingUpdateView

app_name = MailingConfig.name


urlpatterns = [
    path('create/', MailingCreateView.as_view(), name='create'),
    path('mailings/', MailingListView.as_view(), name='list'),
    path('detail/<int:pk>', MailingDetailView.as_view(), name='detail'),
    path('update/<int:pk>', MailingUpdateView.as_view(), name='update'),
    path('delete', MailingDeleteView.as_view(), name='delete'),
]
