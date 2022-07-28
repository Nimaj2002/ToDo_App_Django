from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from .models import ToDoItem


# Create your views here.
# class TodoView(View):
#     def get(self, request):
#         all_todos = ToDoItem.objects.all()
#         return render(request, 'index.html', {'all_todos': all_todos})
#
#     def post(self, request):
#         new_todo = ToDoItem(title=request.POST.get('title'), text=request.POST['todo_text'])
#         new_todo.save()
#         return render(request, 'index.html')

def todo_show(request):
    all_todos = ToDoItem.objects.all()
    return render(request, 'index.html', {'all_todos': all_todos})


def todo_add(request):
    if request.method == 'POST':
        new_todo = ToDoItem(title=request.POST['title'], text=request.POST['text'])
        new_todo.save()
        return HttpResponseRedirect('/')


def todo_delete(request, todo_id):
    if request.method == "POST":
        todo = ToDoItem.objects.get(id=todo_id)
        todo.delete()
        return HttpResponseRedirect('/')

