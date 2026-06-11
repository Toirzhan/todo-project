from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import ToDo


@login_required
def index(request):
    todos = ToDo.objects.all()
    return render(request, 'todoapp/index.html', {'todo_list': todos})


@login_required
@require_http_methods(['POST'])
@csrf_exempt
def add(request):
    title = request.POST['title']
    ToDo.objects.create(title=title)
    return redirect('home')


@login_required
def update(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('home')


@login_required
def delete(request, todo_id):
    ToDo.objects.get(id=todo_id).delete()
    return redirect('home')


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')