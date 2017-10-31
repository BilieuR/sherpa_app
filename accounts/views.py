# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib import auth
from sherpa.models import Profile
from django.contrib.auth import authenticate

# Create your views here.            

def register_view(request):
    if (request.method == 'POST'):
    	first_name = request.POST['first_name']
    	last_name = request.POST['last_name']
    	email = request.POST['email']
    	userType = request.POST['userType']
    	phoneNumber = request.POST['phoneNumber']
        username = request.POST['username']
        password = request.POST['password']


        profile = Profile(first_name=first_name, last_name=last_name, email=email, userType=userType, phoneNumber= phoneNumber, username=username)
        profile.set_password(password)
        print request.POST['admin']
        profile.is_superuser = request.POST['admin']
        profile.save()

    	return render(request, 'register_success.html')
    else:
    	return render(request, 'register.html')


def login_view(request):

	return render(request, 'login.html')


def auth_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
    	auth.login(request, user)
    	return HttpResponseRedirect('/sherpa/loggedin/')
    else:
    	return HttpResponseRedirect('/sherpa/invalid/')


def loggedin_view(request):
    return render(request, 'loggedin.html')


def invalid_view(request):
	return render(request, 'invalid_login.html')


def logout_view(request):
	auth.logout(request)
	return render(request, 'logout.html')
