from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Task

# Create your views here.
# agregar request antes del index.html o cualquier html
def index(request):
    title = 'Django Course !!'
    return render(request, 'index.html', {
        'title': title
    })

# user seria params, y la ruta espera ese parametro
def hello(request, username):
    print(username)
    # %s %variable es declarar una varible dentro de un string de html, param que va cambiando
    return HttpResponse('<h1>hello %s</h1>' %username)

def about(request):
    username = 'Max'
    return render(request, 'about.html', {
        'username': username
    })

# def about(request, id):
#     result = id + 100 * 3
#     return HttpResponse('<h2>about %s</h2>' %result)

def projects(request):
    projects = list(Project.objects.all().values())
    # return JsonResponse(projects, safe=False)
    return render(request, 'projects.html', {
        'projects': projects
    })

def tasks(request):
    # task = Task.objects.get(id=id)
    # buscar por title
    # task = Task.objects.get(title=title)
    # otra forma enviando error 404
    # task = get_object_or_404(Task, id=id)
    # return HttpResponse('task: %s' %task.title)
    task = Task.objects.all()
    return render(request, 'tasks.html', {
        'task': task
    })

