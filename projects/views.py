from django.shortcuts import render,redirect
from django.http import HttpResponse
from .form import ProjectForm, commentForm
from .models import  Project
from django.contrib.auth.decorators import login_required
from .utils import searchProjects, paginatorProjects
from django.contrib import  messages
# Create your views here.


def projects(request):
    projects = Project.objects.all()
    projects, search_query = searchProjects(request)
    projects, paginnation, custome_range = paginatorProjects(request, projects, 6)
    context = {
        'custome_range':custome_range,
        'pagination': paginnation,
        'projects': projects,
        'search_query': search_query
    }
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    project = Project.objects.get(pk=pk)
    reviews = project.review_set.all()
    form = commentForm()
    print(request.method)
    if request.method == 'POST':
        print(request.POST)
        form = commentForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.owner = request.user.profile
            review.project = project
            review.save()
            project.calcutVote()
            messages.success(request, 'successfuly added')
            return redirect('project', pk=project.pk)



    context = {
        'form': form,
        'reviews': reviews,
        'obj': project
    }
    return render(request, 'projects/single-project.html', context)

@login_required(login_url="login")
def create_project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            project = form.save(commit=False)
            print(project.tags)
            project.owner = request.user.profile
            project.save()
            form.save_m2m()
            return redirect('projects')
    context = {
        'form': form,
    }
    return render(request, 'projects/create-update-project.html', context)

@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(pk=pk)
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
    profile = request.user.profile
    project = profile.project_set.get(pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {
        'object': project,
    }
    return render(request, 'delete-temp.html', context)

