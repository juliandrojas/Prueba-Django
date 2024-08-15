from django.urls import path
# Importamos las vistas desde módulo myapp
from . import views
urlpatterns = [
    path('', views.helloWorld),
    path('about/', views.about)    
    
]