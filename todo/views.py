from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.views import View
from .models import Task
from .form import TaskForm


class HomeView(View):
    def get(self, request):
        return render(request, 'todo/index.html', )


class TodoView(View):
    def get(self, request):
        tasksList = Task.objects.all().order_by('-id')
        form = TaskForm()
        return render(request, 'todo/todo.html', {'tasksList': tasksList, "form": form})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/todo')
        else:
            return render(request, 'todo/todo.html',)


class EditView(View):
    def get(self, request, id):
        tasksList = Task.objects.all().order_by('-id')
        task = Task.objects.get(pk=id)
        isEditing = True
        form = TaskForm(instance=task)
        return render(request, 'todo/todo.html', {'tasksList': tasksList, "form": form, 'isEditing': isEditing})

    def post(self, request, id):
        task = Task.objects.get(pk=id)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/todo')
        else:
            return render(request, 'todo/todo.html',)


class DeleteView(View):
    def get(self, request, id):
        task = Task.objects.get(pk=id)
        task.delete()
        return HttpResponseRedirect('/todo')


class CompleteView(View):
    def get(self, request, id):
        task = Task.objects.get(pk=id)
        if task.complete:
            task.complete = False
        else:
            task.complete = True
        task.save()
        return HttpResponseRedirect('/todo')
