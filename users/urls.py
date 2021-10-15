
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('register/', views.registeruser, name='register'),
    path('account/', views.useraccount, name='account'),
    path('edit-account/', views.editaccount, name='edit-account'),
]
