from django.urls import path

from params.apps import ParamsConfig
from params.views import ParamsDeleteView, ParamsCreateView, ParamsDetailView, ParamsUpdateView, ParamsListView

app_name = ParamsConfig.name

urlpatterns = [
    path('message/', ParamsListView.as_view(), name='params_list'),
    path('message/detail/<int:pk>', ParamsDetailView.as_view(), name='detail'),
    path('message/create/', ParamsCreateView.as_view(), name='create'),
    path('message/update/<int:pk>', ParamsUpdateView.as_view(), name='update'),
    path('message/delete/<int:pk>', ParamsDeleteView.as_view(), name='delete'),
]
