from django import forms
from . models import *


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ('student_id', 'sName', 'plateNum', 'idNum', 'vType')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('Fname','Lname', 'Email', 'Uname', 'Pass')