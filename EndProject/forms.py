from django import forms
from .models import User, Task, Team


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        #fields = "__all__"
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
            #if not Email.
               # raise forms.ValidationError("Should contains only letters")
            #return fname

    def clean_password(self):
            #raise forms.ValidationError("Should contains only letters")
            #

    # def clean_age(self):
    #         age = self.cleaned_data["age"]
    #         if age < 18:
    #             raise forms.ValidationError("You must be at least 18.")
    #         return age

class TaskForm(forms.ModelForm):
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
    def clean_title(self):
            Email = self.cleaned_data["username"]
            #if not Email.
               # raise forms.ValidationError("Should contains only letters")
            #return fname

 class TeamForm(forms.ModelForm):
        class Meta:
            model = Team
            fields = ['name']
            labels = {
                "name": "name",

            }

        def clean_name(self):
            Email = self.cleaned_data["username"]
            # if not Email.
            # raise forms.ValidationError("Should contains only letters")
            # return fname
    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
       #  self.fields["kita"].queryset = Kita.objects.filter(can_register=True)

# class EnrollmentForm(forms.ModelForm):
#     class Meta:
#         model = Enrollment
#         fields = ["course", "enrolled_on", "grade"]