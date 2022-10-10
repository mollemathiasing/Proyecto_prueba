from django.urls import path
from home import views

urlpatterns = [
    path ('', views.index),
    path('hola/', views.hola),
    path('fecha/', views.fecha),
    path('fecha-nacimiento/<int:edad>', views.fecha_nacimiento),
    path('mi-template/', views.mi_template),
    path('mi-template/<str:nombre>', views.tu_template),
    path('prueba_template/', views.prueba_template),
    path('ver_personas/', views.ver_personas),
    path('crear_persona/<str:nombre>/<str:apellido>', views.crear_persona),
]



