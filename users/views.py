from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import UserCreation, UpdateProfile, SkillForm
from django.contrib.auth.decorators import login_required
from .utils import searchProfile, paginatorProfiles
# Create your views here.
def loginuser(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        try:
            User.objects.get(username=username)
        except:
            messages.error(request, "username dose not  exist")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)


            return redirect(request.GET.get('next') if 'next' in request.GET else 'profiles')
        else:
            messages.error(request, "username Or password is incorrect")
    return render(request, 'users/login_register.html')

def registeruser(request):
    page = 'register'
    form = UserCreation()
    if request.method == 'POST':
        form = UserCreation(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "user create successfuly")
            login(request, user)
            return redirect('edit-account')
        else:
            messages.error(request, 'Error in registraion')
    context = {
        'form': form,
        'page': page,
    }

    return render(request, 'users/login_register.html', context)


def logoutuser(request):
    logout(request)
    messages.info(request, "logged out successfuly")

    return redirect('login')
def profiles(request):
    profiles = Profile.objects.all()
    profiles, search_query = searchProfile(request)
    profiles, pagination, custome_range = paginatorProfiles(request, profiles, 2)
    context = {
        'custome_range': custome_range,
        'pagination': pagination,
        'profiles': profiles,
        'search_query': search_query
    }
    return render(request, 'users/profiles.html', context)
def userProfile(request, pk):
    profile = Profile.objects.get(pk=pk)
    desskill = profile.skill_set.exclude(description="")
    tagskill = profile.skill_set.filter(description="")
    context = {
        'profile': profile,
        'desskill': desskill,
        'tagskill': tagskill,
    }
    return render(request, 'users/user-profile.html', context)
@login_required(login_url='login')
def useraccount(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    context = {
        'profile': profile,
        'skills': skills,
        'projects': projects,


    }

    return render(request, 'users/account.html', context)

def editaccount(request):
    profile = request.user.profile
    form = UpdateProfile(instance=profile)
    if request.method == 'POST':
        form = UpdateProfile(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {
        'form': form
    }
    return render(request, 'users/edite-account-form.html', context)
def updateSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(pk=pk)
    form = SkillForm(instance=skill)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            skill_pre_save = form.save(commit=False)
            skill_pre_save.owner = profile
            skill_pre_save.save()
            messages.success(request, 'successfully updated')
            return redirect('account')
    context = {
        'form': form
    }
    return render(request, 'users/skill-form.html', context)
def creatSkill(request):
    profile = request.user.profile
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill_pre_save = form.save(commit=False)
            skill_pre_save.owner = profile
            skill_pre_save.save()
            messages.success(request, 'successfully created')
            return redirect('account')
    context = {
        'form': form
    }
    return render(request, 'users/skill-form.html', context)
@login_required()
def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(pk=pk)
    if request.method == "POST":
        skill.delete()
        messages.success(request, 'successfully deleted')
        return redirect('account')
    context = {
        'object': skill
    }
    return render(request, 'delete-temp.html', context)