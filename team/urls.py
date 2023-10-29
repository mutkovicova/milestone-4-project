from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_team_list, name='team')
]
