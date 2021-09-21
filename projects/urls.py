
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.projects, name='projects'),
    path('project/<str:pk>', views.project, name='project'),
    path('create/', views.create_project, name='create'),
    path('update/<str:pk>', views.updateProject, name='update'),
    path('delete/<str:pk>', views.deleteProject, name='delete'),
]
