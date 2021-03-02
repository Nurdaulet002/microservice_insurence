from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name = 'directory'

urlpatterns = [
    path('insurance/list', views.InsuranceListView.as_view(), name='insurence_list'),
    path('insurance/create', views.InsuranceCreateView.as_view(), name='insurence_create'),
    path('insurance/update/<int:pk>', views.InsuranceUpdateView.as_view(), name='insurance_update'),
    path('insurance/delete/<int:pk>', views.InsuranceDeleteView.as_view(), name='insurance_delete'),
    path('insurer/list', views.InsurerListView.as_view(), name='insurer_list'),
    path('insurer/create', views.InsurerCreateView.as_view(), name='insurer_create'),
    path('insurer/update/<int:pk>', views.InsurerUpdateView.as_view(), name='insurer_update'),
    path('insurer/delete/<int:pk>', views.InsurerDeleteView.as_view(), name='insurer_delete'),
    path('service/list', views.ServiceListView.as_view(), name='service_list'),
    path('service/create', views.ServiceCreateView.as_view(), name='service_create'),
    path('service/update/<int:pk>', views.ServiceUpdateView.as_view(), name='service_update'),
    path('service/delete/<int:pk>', views.ServiceDeleteView.as_view(), name='service_delete'),
]
