from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from .models import ToDoItem


def todo_show(request):
    all_todos = ToDoItem.objects.all()
    return render(request, 'todo_list.html', {'all_todos': all_todos})


def todo_add(request):
    if request.method == "GET":
        return render(request, 'add_todo.html')
        
    if request.method == 'POST':
        new_todo = ToDoItem(title=request.POST['title'], text=request.POST['text'])
        new_todo.save()
        return HttpResponseRedirect('/')


def todo_delete(request, todo_id):
    if request.method == "POST":
        todo = ToDoItem.objects.get(id=todo_id)
        todo.delete()
        return HttpResponseRedirect('/')

