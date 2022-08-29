from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm
def home(request):
    todos = Todo.objects.all()
    context = {
        "todos" : todos
    }

    return render(request, "todo/home.html", context)

def todo_create(request):
    form = TodoForm()
    if request.method= "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {
        "form" : form
    }
    return render(request, "todo/todo_add.html", context)