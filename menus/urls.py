from django.urls import path
from . import views

urlpatterns = [
    path('get-menu', views.get_menu, name='get_menu'),
    path('today', views.today, name='today'),
]