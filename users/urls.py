
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
]
