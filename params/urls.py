from django.urls import path

from params.apps import ParamsConfig
from params.views import ParamsDeleteView, ParamsCreateView, ParamsDetailView, ParamsUpdateView, ParamsListView

app_name = ParamsConfig.name

urlpatterns = [
    path('params/', ParamsListView.as_view(), name='params_list'),
    path('params/detail/<int:pk>', ParamsDetailView.as_view(), name='detail'),
    path('params/create/', ParamsCreateView.as_view(), name='create'),
    path('params/update/<int:pk>', ParamsUpdateView.as_view(), name='update'),
    path('params/delete/<int:pk>', ParamsDeleteView.as_view(), name='delete'),
]
