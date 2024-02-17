from django.shortcuts import render,HttpResponse,redirect
from .models import Task
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def home(request):
    return render(request,'home.html')

def to_do(request):
    tasks = Task.objects.filter(is_deleted=0)
    return render(request, 'todo_new.html', {'tasks': tasks})



def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})
    
@csrf_exempt
def add_task(request):
    if request.method == 'POST':
        # title = request.POST['title']
        # description = request.POST['description']
        # category_id = request.POST['category_id']
        task = Task(title="Enter Title", description="Enter Description",is_deleted=0)
        task.save()
        return redirect('to_do')
    return render(request, 'add_task.html')

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('to_do')

@csrf_exempt
def update(request):
    if request.method == 'POST' :
        data = json.loads(request.body)
        task_id=data.get('task_id')
        field = data.get('field')
        value = data.get('value')
        
        try:
            task = Task.objects.get(id=task_id)   
            setattr(task, field, value)
            task.save()
            return JsonResponse({'message': 'Task updated successfully'}, status=200)
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Task not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def delete(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        task_id = data.get('task_id')
        try:
            task = Task.objects.get(id=task_id)
            setattr(task,'is_deleted',1)
            task.save()
            return JsonResponse({'message': 'Task deleted successfully'}, status=200)
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Task not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)