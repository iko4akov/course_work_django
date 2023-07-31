from django.urls import path

from params.apps import ParamsConfig
from params.views import ParamsDeleteView, ParamsCreateView, ParamsDetailView, ParamsUpdateView, ParamsListView

app_name = ParamsConfig.name

urlpatterns = [
    path('', ParamsListView.as_view(), name='params_list'),
    path('view/<int:pk>', ParamsDetailView.as_view(), name='view'),
    path('create/', ParamsCreateView.as_view(), name='create'),
    path('update/<int:pk>', ParamsUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ParamsDeleteView.as_view(), name='delete'),
]
