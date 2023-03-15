from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PointForm


# Create your views here.


def home(response):
	return render(response, "main/home.html", {})



