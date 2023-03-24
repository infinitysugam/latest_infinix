from django.shortcuts import render,HttpResponse,redirect
from .models import Task
# Create your views here.
def home(request):
    return render(request,'home.html')

def to_do(request):
    tasks = Task.objects.all()
    return render(request, 'to_do.html', {'tasks': tasks})



def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        category_id = request.POST['category_id']
        task = Task(title=title, description=description,category_id=category_id)
        task.save()
        return redirect('to_do')
    return render(request, 'add_task.html')

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('to_do')