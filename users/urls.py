
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
    path('update-skill/<str:pk>/', views.updateSkill, name='update-skill'),
    path('update-skill/', views.creatSkill, name='create-skill'),
    path('delete-skill/<str:pk>', views.deleteSkill, name='delete-skill'),
    path('inbox/', views.inbox, name='inbox'),
    path('message/<str:pk>', views.message, name='single-message'),
    path('send_message/<str:pk>', views.send_message, name='send-message'),

]
