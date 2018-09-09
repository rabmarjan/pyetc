from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info('Start reading database')


# Create your views here.

def index(request):
    todos = Todo.objects.all()
    context = {"todos": todos}
    logger.info('Start reading database')
    return render(request, "index.html", context)


def detail(request, id):
    todo = Todo.objects.get(id=id)
    context = {"todo": todo}
    return render(request, "details.html", context)


def add(request):
    if request.method == "POST":
        title = request.POST["title"]
        text = request.POST["text"]
        todo = Todo(title=title, text=text)
        todo.save()
        return redirect("/todos")
    else:
        return render(request, 'add.html')
