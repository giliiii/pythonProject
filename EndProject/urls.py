from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    #user:
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path('list/', views.user_list, name='person_list'),
    path('choose/', views.chooseTeam, name='chooseTeam'),

    #team


    #task:
    path("tasks/", views.tasks, name="tasks"),
    path('tasks/add/', views.task_create, name='task_create'),
    path('tasks/edit/<int:pk>/', views.task_update, name='task_update'),
    path('tasks/delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('tasks/task_take/', views.task_take, name='task_take'),


]