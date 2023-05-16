from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject

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

def create_task(request):
    # pasar por consola el metodo get de los datos, porque form no tiene un action especifica
    # print(request.GET['title'])
    if request.method == 'GET':
        # show interface
        return render(request, 'create_task.html', {
            'form': CreateNewTask
        })
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
        # url = render
        return redirect('/tasks/')
    

def create_project(request):
    if request.method == 'GET':
        # show interface
        return render(request, 'create_project.html', {
            'form': CreateNewProject
        })
    else:
        project = Project.objects.create(name=request.POST['name'])
        return redirect('create_project')
    

def project_detail(request, id):
    project = get_object_or_404(Project,id=id)
    tasks = list(Task.objects.filter(project_id=id).values())
    print(project)
    return render(request, 'detail.html', {
        'project': project,
        'tasks': tasks
    })