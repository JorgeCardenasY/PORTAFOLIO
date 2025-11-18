from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('analytics/', views.analytics, name='analytics'),
    path('contact/', views.contact, name='contact'),
    path('proyectos/', views.proyectos, name='proyectos'),
]
