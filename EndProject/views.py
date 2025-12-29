from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Task,Team
from .forms import UserForm, TaskForm, TeamForm
#from django.http import Http404
from django.db import transaction

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required


# REGISTER
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after register
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {"form": form})


# LOGIN
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect("login")



@login_required
@transaction.atomic
def User_create(request):
    if request.method == "POST":
        formUser = UserForm(request.POST)
        # formTask = TaskForm(request.POST)
        if formUser.is_valid():
            #1 - Save to User
            newUser = formUser.save()
            newUser.save()
            #2 - Save to Task and connect tp User
            # # Task = formTask.save(commit=False)
            # Task.User = User
            # Task.save()
            #3 - Save the n:m relationship
            # formTask.save_m2m()

            return redirect('User_list')
    else:
        formUser = UserForm()
        # formTask = TaskForm()
    form = formUser  # combine them
    return render(request, 'Users/User_form.html', {'form': form})

@login_required
@transaction.atomic
def Task_create(request):
    if request.method == "POST":
        formTask = TaskForm(request.POST)
        # formTask = TaskForm(request.POST)
        if formTask.is_valid():
            #1 - Save to User
            newTask = formTask.save()
            newTask.save()
            #2 - Save to Task and connect tp User
            # # Task = formTask.save(commit=False)
            # Task.User = User
            # Task.save()
            #3 - Save the n:m relationship
            # formTask.save_m2m()

            return redirect('Task_list')
    else:
        formTask = TaskForm()
        # formTask = TaskForm()
    form = formTask  # combine them
    return render(request, 'Users/User_form.html', {'form': form})


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

@login_required
def Task_list(request):
    Tasks = Task.objects.all()
    return render(request, 'Users/User_list.html', {'tasks': Tasks})

@login_required
def User_update(request, tz):
    User = get_object_or_404(User, pk=tz)

    ##alternative code
    #User = User.objects.filter(tz=tz).first()
    #if not User:
    #    raise Http404("User not found")

    #syntax for get_object_or_404
    #get_object_or_404(Model, pk=value)
    #get_object_or_404(Model, field=value)
    #get_object_or_404(Model, field__lookup=value)
    #get_object_or_404(queryset, filter=value)

    if request.method == "POST":
        form = UserForm(request.POST, instance=User)
        if form.is_valid():
            form.save()
            return redirect('User_list')
    else:
        form = UserForm(instance=User)

    return render(request, 'Users/User_form.html', {'form': form})


@login_required
def User_delete(request, tz):
    User = get_object_or_404(User, pk=tz)

    if request.method == "POST":
        User.delete()
        return redirect('User_list')

    return render(request, 'Users/User_confirm_delete.html', {'User': User})

# Create your views here.
