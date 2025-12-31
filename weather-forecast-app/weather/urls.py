from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('weather/', views.get_weather, name='get_weather'),
    path('history/', views.search_history, name='history'),
       path('history/clear/', views.clear_history, name='clear_history'),
]