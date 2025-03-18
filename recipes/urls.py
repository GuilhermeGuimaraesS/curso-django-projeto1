from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home
    path('sobre/', views.sobre, name='sobre'),  # Sobre
    path('contato/', views.contato, name='contato'),  # Contato
]
