from django.shortcuts import render, redirect
from . import forms
from . models import Task
from django.contrib import messages
from django.views import View

# Create your views here.

class RegistrationView(View):
    def get(self, request):
        form = forms.RegistrationForm
        return render(request, '', locals())

    def post(self, request):
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Congratulations! User Registered Successfully"
            )
            return redirect('')


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
        form.owner = request.user
        return render(request, '', locals())

    def post(self, request):
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Congratulations! Task Created Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return redirect('')