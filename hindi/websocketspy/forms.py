from django.forms import ModelForm
from .models import AttendanceModel, AddEmployee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class AttendanceModelForm(ModelForm):
    class Meta:
        model = AttendanceModel
        fields = "__all__"

class AddEmployeeForm(ModelForm):
    class Meta:
        model = AddEmployee
        fields = "__all__"


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", 'password2']