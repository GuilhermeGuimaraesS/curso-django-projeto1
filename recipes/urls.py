from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home
    path('recipes/<int:id>/', views.recipe, name='recipe'), # Recipe page
]
