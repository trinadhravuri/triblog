from django.shortcuts import render,redirect
from .models import Projects
from .forms import ProjectsForm
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.


def base(request):
    return render(request,'projectsblog/base.html')

def allprojects(request):
    projects = Projects.objects.all()
    context={
        'projects':projects,
    }
    return render(request,'projectsblog/allprojects.html',context)

def addproject(request):
    form = ProjectsForm
    if request.method == 'POST':
        form = ProjectsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(allprojects)
    context ={
        'form':form
    }
    return render(request,'projectsblog/addproject.html',context)