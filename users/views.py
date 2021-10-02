from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def loginuser(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        try:
            User.objects.get(username=username)
        except:
            print("username dosent exist")
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            print(user)
            login(request, user)
            return redirect('profiles')
        else:
            print("sik kon koony")
    return render(request, 'users/login_register.html')

def logoutuser(request):
    logout(request)
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