from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect
from .forms import CreateNewTask
# Create your views here.
def index(request):
    title = 'Django Course!!'
    return render(request,'index.html', {'title' : title})

def hello(request, username):
    #? Saber el tipo de dato
    #?print(type(id))
    #?result = id + 100 + 2
    return HttpResponse("Hello %s" %username)

def about(request):
    username = 'ureyes'
    return render(request, 'about.html', {'username' : username})

def projects(request):
    projects = list(Project.objects.values())
    return render(request, 'projects.html', {'projects': projects})

def task(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html',{'tasks' : tasks})

def create_Task(request):
    if request.method == 'GET':
        # SHOW INTERFACE
        return render(request, 'create_task.html', {'form': CreateNewTask()})
    else:
        title = request.POST['title']
        description = request.POST['description']
        Task.objects.create(title = title, description = description, project_id = 2)
        return redirect('/tasks/')