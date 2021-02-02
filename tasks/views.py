from django.shortcuts import render,redirect
from .models import *
from .forms import *

def index(request):
    tasks = Task.objects.all()
    form = Taskform()

    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'tasks':tasks, 'form':form}
    return render(request, 'tasks/index.html',context)

def update(request, pk):
    tasks = Task.objects.get(id=pk)
    form = Taskform(instance=tasks)
    if request.method == 'POST':
        form = Taskform(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'tasks':tasks,'form':form}
    return render(request, 'tasks/update_task.html',context)

def delete(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item':item}

    return render(request, 'tasks/delete.html',context)
