from django import forms
from django.contrib.auth.forms import UserCreationForm

from new_app.models import Login, Student, admregister, Mark


class DateInput(forms.DateInput):
    input_type = 'date'


class Login_form(UserCreationForm):
    class Meta :
        model=Login
        fields = ("username","password1",'password2')

class studentregister(forms.ModelForm):
    dob = forms.DateField(widget=DateInput)

    class Meta:
        model = Student
        fields = '__all__'
        exclude=("user",)


class adminregister(forms.ModelForm) :
    dob = forms.DateField(widget=DateInput)

    class Meta:
        model = admregister
        fields = '__all__'
        exclude = ("user",)


class MarkForm(forms.ModelForm):

    class Meta:
        model = Mark
        fields = '__all__'


