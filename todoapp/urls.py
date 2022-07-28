from django.urls import path

from .views import todo_show, todo_add, todo_delete

urlpatterns = [
    path('', todo_show),
    path('add/', todo_add),
    path('delete/<int:todo_id>/', todo_delete),
]
