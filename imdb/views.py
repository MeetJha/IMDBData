from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie_Data
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
	if request.user.is_authenticated:
		data1 = Movie_Data.objects.all()
		return render(request, 'index.html', {'data1': data1})
	else:
		return redirect('/login')
	
def sort_by_name(request):
	if request.user.is_authenticated:	
		data1= Movie_Data.objects.all().order_by('movie_title')
		return render(request, 'index.html', {'data1': data1})	 	
	else:
		return redirect('/login')

def sort_by_rating(request):
	if request.user.is_authenticated:
		data1= Movie_Data.objects.all().order_by('-movie_rating')
		return render(request, 'index.html', {'data1': data1})	 	
	else:
		return redirect('/login')
	

def sort_by_release_date(request):
	if request.user.is_authenticated:
		data1= Movie_Data.objects.all().order_by('-movie_release_date')
		return render(request, 'index.html', {'data1': data1})	 	
	else:
		return redirect('/login')

def sort_by_duration(request):
	if request.user.is_authenticated:
		data1= Movie_Data.objects.all().order_by('movie_duration')
		return render(request, 'index.html', {'data1': data1})	 	
	else:
		return redirect('/login')

def login(request):
	return render(request, 'login.html')

def check_login(request):
	if request.method =="POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('/index')
	else:
		return redirect('/login')

def logout(request):
	auth.logout(request)
	return redirect('/login')


