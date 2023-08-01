from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="inicio"),

    path('adoptantes/', adoptantes, name="adoptantes"),
    path('gatitos/',lista_gatitos, name="lista_gatitos"),
    path('personal/', lista_personal, name="lista_personal"),

    path('agregar_gatito/',agregar_gatito, name='agregar_gatito'),
    path('agregar_adoptante/',agregar_adoptante, name='agregar_adoptante'),
    path('agregar_personal/',agregar_personal, name='agregar_personal'),

    path('buscar_gatito/', buscar_gatito, name='buscar_gatito'),
    

]
