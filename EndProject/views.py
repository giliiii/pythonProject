from django.shortcuts import render, redirect, get_object_or_404
from docutils.parsers.rst.directives.misc import Role

from .models import User, Task,Team
from .forms import UserForm, TaskForm, TeamForm,CustomUserCreationForm,CustomAuthenticationForm,ChooseTeamForm
#from django.http import Http404
from django.db import transaction

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required


# REGISTER
def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after register
            return redirect("chooseTeam")
    else:
        form = CustomUserCreationForm()
    return render(request, "users/register.html", {"form": form})


# LOGIN
def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = CustomAuthenticationForm()
    return render(request, "users/login.html", {"form": form})


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect("home")





@login_required
@transaction.atomic
def task_create(request):
    if request.user.role != "admin":
        return redirect("tasks")

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.myTeam=request.user.team
            form.save()
            return redirect('tasks')
    else:
        form = TaskForm()

    return render(request, 'tasks/createTask.html', {'form': form})


@login_required
def Team_enroll(request,team_name):
    team = get_object_or_404(Team,NAME=team_name)
    if request.method == "POST":
        user_id=request.POST.get("username")
        user = get_object_or_404(User,NAME=user_name)
        user.team=team
        user.save()
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.Task = Task
            enrollment.save()
    else:
        form = EnrollmentForm()
    return render(request, 'Users/enroll_form.html', { "Task": Task,'form': form})

@login_required
def User_list(request):
    Users = User.objects.all()
    return render(request, 'Users/User_list.html', {'Users': Users})




# Create your views here.
def home(request):
    return render(request, 'home.html', )

def user_list(request):
    Users = User.objects.all()
    return render(request, 'userList.html', {'User': User})


def tasks(request):

    user=request.user
    tasks = Task.objects.filter(myTeam=user.team)
    status = request.GET.get('status')
    if status:
        tasks = tasks.filter(status=status)

    employee_name = request.GET.get('employee_name')
    if employee_name:
        tasks = tasks.filter(assigned_to__name__icontains=employee_name)
    return render(request, "tasks/taskList.html",{'Tasks': tasks})


@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)

    # בדיקה למנהל
    if request.user.role == "admin" and task.myDoner is None :
        if request.method == "POST":
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect('tasks')
        else:
            form = TaskForm(instance=task)
        return render(request, 'tasks/crateTask.html', {'form': form})
    else:
        return redirect('tasks')  # חסום משתמש שלא מורשה

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.user.role == "admin" and task.myDoner is None:
        if request.method == "POST":
            task.delete()
            return redirect('tasks')
        return render(request, 'tasks/deleteTask.html', {'task': task})
    else:
        return redirect('tasks')

@login_required
def task_take(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task.myDoner is None and request.user.role == "worker":
        task.myDoner = request.user
        task.status="Process"
        task.save()
    return redirect('tasklist')

@login_required
def task_finish(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task.myDoner ==request.user and task.status == "Process":
        task.status="Process"
    return redirect('tasks')

@login_required
def chooseTeam(request):
    if request.method == "POST":
        form = ChooseTeamForm(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            role = form.cleaned_data['role']
            user = request.user
            user.role = role
            user.myTeam = team
            user.save()
            return redirect("home")
    else:
            form = ChooseTeamForm()
    return render(request, "users/chooseTeam.html", {"form": form})

