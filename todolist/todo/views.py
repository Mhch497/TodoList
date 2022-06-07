from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


def index(request):
    global checks
    tasks = Task.objects.all()
    cats = Category.objects.all()
    error = ''
    done_tasks = Task.objects.filter(is_done=True)
    if request.method == 'POST' and len(tasks) != 0:
        checks = request.POST.getlist('checkbox')
        for check in checks:
            task = Task.objects.get(id=check)
            task.is_done = True
            task.save()
            return redirect('home')
    context = {

        'title': 'Все задачи',
        'tasks': tasks,
        'cats': cats,
        'error': error,
        'done_tasks': done_tasks
    }
    return render(request, 'todo/index.html', context)


def cats(request):
    cats = Category.objects.all()
    error = ''
    if request.method == 'POST':
            name = request.POST['name']
            if cats.filter(name=name).exists():
                error = 'Такая категория уже есть'
            elif name == "Введите категорию" or name == '':
                error = 'Необходимо ввести категорию'
            else:
                category = Category(name=name)
                category.save()
                return redirect('cats')
    context = {
        'title': 'Категории',
        'cats': cats,
        'error': error,
    }
    return render(request, 'todo/categories.html', context)


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверно заполнена'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'todo/addTask.html', context)


def task(request, taskid):
    task = get_object_or_404(Task, id=taskid)
    cats = Category.objects.all()

    prompt = ''
    if request.method == 'POST':
        if 'delete' in request.POST:
            task.delete()
            return redirect('home')
        elif 'change' in request.POST:
            if 'checkbox' not in request.POST:
                task.is_done = False
                task.save()
            task.task = request.POST['name']
            task.category = Category.objects.get(id=request.POST['cat'])
            task.content = request.POST['content']
            task.data_todo = request.POST['date']
            task.save()
            prompt = 'Ваши изменения успешно сохранены'
            return redirect('home')

    form = TaskForm()
    context = {
        'title': task.task,
        'task': task,
        'cats': cats,
        'cat': task.category,
        'form': form,
        'prompt': prompt,
    }
    return render(request, 'todo/task.html', context)

def category(request, catid):
    cat = get_object_or_404(Category, id=catid)
    tasks = Task.objects.all()
    cats = Category.objects.all()
    prompt = ''
    if request.method == 'POST':
        if 'delete' in request.POST:
            Task.objects.filter(category=cat).delete()

            cat.delete()
            return redirect('home')
        elif 'update' in request.POST:
            if 'checkbox' in request.POST:
                checks = request.POST.getlist('checkbox')
                for check in checks:
                    task = Task.objects.get(id=check)
                    task.is_done = True
                    task.save()
            cat.name = request.POST['name']
            cat.save()
            return redirect('home')
    context = {
        'title': cat.name,
        'tasks': tasks,
        'cat': cat,
        'cats': cats,
        'prompt': prompt,
    }
    return render(request, 'todo/category.html', context)


