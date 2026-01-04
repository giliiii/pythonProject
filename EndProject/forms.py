from django import forms
from .models import User, Task, Team
from datetime import datetime, timedelta
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        # fields = "__all__"
        labels = {
            "username": "Email",
            "password": "password",
        }
        help_texts = {
            "f_name": "Should be valid email adress",
            "l_name": "Should contains letters and numbers",
        }

    def clean_username(self):
        Email = self.cleaned_data["username"]
        # if not Email.
        #     raise forms.ValidationError("Should contains only letters")
        # return fname


# def clean_password(self):


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={'type': 'datetime-local'}  # חץ לבחירת תאריך ושעה
        ),
        initial=(datetime.now() + timedelta(days=30)).strftime("%Y-%m-%dT%H:%M"))
    myTeam = forms.ModelChoiceField(Team.objects.all())
    myDoner = forms.ModelChoiceField(User.objects.all())
    class Meta:
        model = Task
        fields = "__all__"
        labels = {
            "title": "title",
            "describe": "describe",
            "myTeam": "myTeam",
            "status": "status",
            "myDoner": "myDoner",
            "deadline": "deadline",
        }
        help_texts = {
            "f_name": "Should be valid email adress",
            "l_name": "Should contains letters and numbers",
        }


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name']
        labels = {
            "name": "name",
        }

    # def clean_name(self):
    #     Email = self.cleaned_data["username"]
    #     if not Email.
    #         raise forms.ValidationError("Should contains only letters")
    #     return fname

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields["kita"].queryset =
        # Kita.objects.filter(can_register=True)



class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'password1','password2']


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class ChooseTeamForm(forms.Form):
    team = forms.ModelChoiceField(queryset=Team.objects.all(), empty_label="Select a team")
    role = forms.ChoiceField(choices=[('admin', 'Admin'), ('worker', 'Worker')])
# class EnrollmentForm(forms.ModelForm):
#     class Meta:
#         model = Enrollment
#         fields = ["course", "enrolled_on", "grade"]