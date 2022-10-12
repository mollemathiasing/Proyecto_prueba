from django.urls import path
from home import views

urlpatterns = [
    path ('', views.index, name = 'index'),
    path('hola/', views.hola, name = 'hola'),
    path('fecha/', views.fecha, name = 'fecha'),
    path('fecha-nacimiento/<int:edad>', views.fecha_nacimiento),
    # path('mi-template/', views.mi_template, name = 'mi_template'),
    path('mi-template/<str:nombre>', views.tu_template),
    path('prueba_template/', views.prueba_template),
    path('ver_personas/', views.ver_personas, name = 'ver_personas'),
    path('crear_persona', views.crear_persona, name = 'crear_persona'),
]



