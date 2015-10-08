from django.contrib import auth
from django.http import *

def login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = auth.authenticate(username=username, password=password)
	if user is not None and user.is_active:
		auth.login(request, user)
		return HttpResponsePermanentRedirect('')
	else:
		return HttpResponsePermanentRedirect('')



def logout(request):
    auth.logout(request)
    # Перенаправление на страницу.
    return HttpResponseRedirect("/account/loggedout/")

def is_true(request, username):
	return render(request, 'blog/account/registration.html')

def is_false(request):
	return render(request, 'blog/account/registration.html')