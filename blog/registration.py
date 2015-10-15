from django.contrib import auth
from django.shortcuts import render
from django.http import *

def login(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	if user is not None and user.is_active:
		auth.login(request, user)
		return HttpResponsePermanentRedirect('/personal/'+username+'/')
	else:
		return HttpResponsePermanentRedirect('/')



def logout(request):
    auth.logout(request)
    # Перенаправление на страницу.
    return HttpResponseRedirect("/")

def is_true(request, id):
	return render(request, 'blog/account/registration.html')

def is_false(request):
	return render(request, 'blog/account/registration.html')