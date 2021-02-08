from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from django.utils import timezone
from .forms import *


# Create your views here.


def index(request):
    get_todo = Todo.objects.all().order_by('-added_date')
    form = TodoForm()
    template = 'to_do/index.html'
    context = {
        'get_todo': get_todo,
        'form': form
    }

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('to_do:index')

    return render(request, template, context)


def deletetodo(request):
    todo_id = request.POST['delete_id']
    get_object_or_404(Todo, pk=todo_id).delete()
    return redirect('to_do:index')


def updatetodo(request, task_id):
    task = get_object_or_404(Todo, pk=task_id)
    form = TodoForm(instance=task)
    template = 'to_do/update.html'
    context = {
        'form': form
    }

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('to_do:index')

    return render(request, template, context)
