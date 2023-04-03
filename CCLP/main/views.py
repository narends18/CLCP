from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import PointForm, AddStudentForm, AddClassForm, AddPointsForm
from .models import Student, Class, Person


# Create your views here.

@login_required(login_url="login")
@user_passes_test(lambda user: user.groups.filter(name__in=["Staff", "Admin"]).exists())
def index(request):
	students = User.objects.filter(groups__name="Student")
	classes = Class.objects.all()
	return render(request, "main/home.html", {"students":students, "classes": classes})

@login_required(login_url = "login")
@user_passes_test(lambda user: user.groups.filter(name__in=["Staff", "Admin"]).exists())
def add_student(request):
	if request.method == 'POST':
		form = AddStudentForm(request.POST)
		if form.is_valid():
			user = form.save(commit = False)
			user.set_password(user.password)
			user.groups.add(Group.objects.get(name='student'))
			user.save()
			messages.success(request, "Student added successfully!")
			return redirect("index")
	else:
		form = AddStudentForm()
	return render(request, "main/add_student.html")

	









