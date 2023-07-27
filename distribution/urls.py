from django.urls import path

from distribution.apps import DistributionConfig
from distribution.views import DistributionListView, DistributionDetailView, DistributionCreateView, DistributionUpdateView, DistributionDeleteView

app_name = DistributionConfig.name

urlpatterns = [
    path('', DistributionListView.as_view(), name='distribution_list'),
    path('view/<int:pk>', DistributionDetailView.as_view(), name='view'),
    path('create/', DistributionCreateView.as_view(), name='create'),
    path('update/<int:pk>', DistributionUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', DistributionDeleteView.as_view(), name='delete'),
]