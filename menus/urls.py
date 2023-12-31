from django.urls import path
from . import views

urlpatterns = [
    path('get-menu', views.get_menu, name='get_menu'),
    path('today-breakfast', views.today_breakfast, name='today_breakfast'),
    path('today-dinner', views.today_dinner, name='today_dinner'),
]