from django.urls import path
from . import views

urlpatterns = [
    path('get-menu', views.get_menu, name='get_menu'),
    path('today', views.get_today, name='today'),
    path('validate-date', views.validate_date, name='validate-date'),

    path('getusageinfo', views.get_usage_info, name='get_usage_info')
]