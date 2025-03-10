from . import views
from django.urls import path

urlpatterns = [
    path('', views.redirect_to_home),
    path('task-manager/view-list/', views.task_list, name='task_list'),

    path('create/', views.task_create, name='task_create'),
    path('task-manager/<int:id>/edit/', views.task_update, name='task_update'),
    path('task-manager/<int:id>/delete/', views.task_delete, name='task_delete'),

]
