from django.shortcuts import render, redirect
from . import forms
from . models import Task
from django.contrib import messages
from django.views import View

# Create your views here.

class RegistrationView(View):
    def get(self, request):
        form = forms.RegistrationForm
        v = True
        return render(request, 'connexion.html', locals())

    def post(self, request):
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Congratulations! User Registered Successfully"
            )
            return redirect('login')


def DelteteTask(request, pk):
    task = Task.objects.get(pk = pk)
    if task.delete():
        messages.success(request, "Task Deleted Successfully!")
    else:
        messages.warning(request, "Unable To Delete This Task!")
    return redirect('')


class CreateTask(View):
    def get(self, request):
        form = forms.TaskForm
        return render(request, 'create.html', locals())

    def post(self, request):
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            Task.objects.create(request.user, form.label, form.descritpion, form.begin, form.end, form.priority, form.done)
            messages.success(
                request, "Congratulations! Task Created Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return redirect('tasks')
    

class UpdateTask(View):
    def get(self, request, pk):
        form = forms.TaskForm
        key = Task.objects.get(pk=pk)
        return render(request, 'update.html', locals())
    
    def post(self, request, pk):
        form = forms.TaskForm(request.POST)
        task = Task.objects.get(pk=pk)
        if form.is_valid():
            task.label = form.cleaned_data['label']
            task.description = form.cleaned_data['description']
            task.begin = form.cleaned_data['begin']
            task.end = form.cleaned_data['end']
            task.priority = form.cleaned_data['pritority']
            task.done = form.cleaned_data['done']

            task.save()

            messages.success(request, "Congratulations! Task Updated Successfully")
            return redirect('update')
        else:
            messages.warning(request, "Invalid Input Data")
            return redirect('tasks')
    

def TaskView(request, *args, **kwargs):
    if request.user.is_authenticated:
        task = Task.objects.filter(owner = request.user)
        if task == []:
            empty = "You have no tasks."
        return render(request, 'tasks.html', locals())
    else:
        return redirect('login')
