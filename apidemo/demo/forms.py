from django import forms

from demo.models import Student


class Stdudent_form(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['std_name', 'std_email', 'std_contact']