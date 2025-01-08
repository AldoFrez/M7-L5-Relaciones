from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='uno_a_uno_index'), # me traigo la funcion indexde views
]