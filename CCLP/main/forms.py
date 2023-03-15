from django import forms
from django.contrib.auth.models import User, Group
from .models import Person, Class, Student

class PointForm(forms.ModelForm):
	teacher = forms.ModelChoiceField(queryset=User.objects.filter(is_staff = True))
	class_name = forms.ModelChoiceField(queryset=Class.objects.all())
	student = forms.ModelChoiceField(queryset=User.objects.exclude(is_staff = True))

	class Meta:
		model = Person
		fields = ("student", "class_name", "teacher", "points", "description")


class AddStudentForm(forms.ModelForm):
	class Meta:
		model = Student 

		fields = ("username",)


class AddClassForm(forms.ModelForm):
	class Meta:
		model = Class
		fields = ("name",)


class AddPointsForm(forms.ModelForm):
	class_name = forms.ModelChoiceField(queryset = Class.objects.all())
	student = forms.ModelChoiceField(queryset = User.objects.exclude(is_staff = True, is_superuser = True))



