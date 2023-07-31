from django.shortcuts import render, redirect

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import TodoModel


def index(request):
    todos = TodoModel.objects.all()
    return render(request, 'todolist/home.html', {"todo_list": todos})


@require_http_methods(['POST'])
@csrf_exempt
def add(request):
    title = request.POST['title']
    description = request.POST['description']
    todo = TodoModel(title=title, description=description)
    todo.save()
    return redirect('home')


def update(request, todo_id):
    todo = TodoModel.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('home')


def delete(request, todo_id):
    todo = TodoModel.objects.get(id=todo_id)
    todo.delete()
    return redirect('home')
