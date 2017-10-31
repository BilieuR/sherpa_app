# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib import auth
from sherpa.models import Users
from django.contrib.auth import authenticate

# Create your views here.            

def register_view(request):
    if (request.method == 'POST'):
    	firstName = request.POST['firstName']
    	familyName = request.POST['familyName']
    	email = request.POST['email']
    	userType = request.POST['userType']
    	phoneNumber = request.POST['phoneNumber']
        username = request.POST['username']
        password = request.POST['password']

        users = Users(firstName=firstName, familyName=familyName, email=email, userType=userType, phoneNumber= phoneNumber, username=username, password=password)
        #users.set_password(password)
        users.save()

    	return render_to_response('register_success.html')
    else:
    	return render_to_response('register.html')


def login_view(request):

	return render_to_response('login.html')


def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/sherpa/loggedin')
	else:
		return HttpResponseRedirect('/sherpa/invalid')


def loggedin_view(request):
	return render_to_response('loggedin.html', {'full_name': request.user.username})


def invalid_view(request):
	return render_to_response('invalid_login.html')


def logout_view(request):
	auth.logout(request)
	return render_to_response('logout.html')
