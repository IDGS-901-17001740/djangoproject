from django.urls import path
#? Importar desde . es decir que es en la carpeta actual
from . import views
urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    #?Params en la url
    path('hello/<str:username>', views.hello),
    path('projects/projects/', views.projects),
    path('tasks/tasks/', views.task),
    path('tasks/create_task/', views.create_Task),
    path('projects/create_project', views.create_project)
]