from django.urls import path
#? Importar desde . es decir que es en la carpeta actual
from . import views
urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    #?Params en la url
    path('hello/<str:username>', views.hello),
    path('projects/', views.projects),
    path('task/<int:id>', views.task),
]