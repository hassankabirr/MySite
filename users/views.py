from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import UserCreation, UpdateProfile
from django.contrib.auth.decorators import login_required
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
        print(user)
        if user is not None:
            print(user)
            login(request, user)
            return redirect('profiles')
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
            return redirect('profiles')
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
    context = {
        'profiles': profiles
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