from django.shortcuts import render,redirect
from django.http import HttpResponse
from .form import ProjectForm
from .models import  Project
from django.contrib.auth.decorators import login_required
# Create your views here.


def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'obj': project
    }
    return render(request, 'projects/single-project.html', context)

@login_required(login_url="login")
def create_project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {
        'form': form,
    }
    return render(request, 'projects/create-update-project.html', context)

@login_required(login_url="login")
def updateProject(request, pk):
    project = Project.objects.get(pk=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        print(request.POST)
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {
        'form': form,
    }

    return render(request, 'projects/create-update-project.html', context)

@login_required(login_url="login")
def deleteProject(request, pk):
    project = Project.objects.get(pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {
        'object': project,
    }
    return render(request, 'projects/create-update-project.html', context)