from django.contrib import auth

def login(request):
    username = request.POST['email']
    password = request.POST['password']
    user = auth.authenticate(email=email, password=password)
    if user is not None and user.is_active:
        # Правильный пароль и пользователь "активен"
        auth.login(request, user)
        # Перенаправление на "правильную" страницу
        return HttpResponseRedirect("/account/loggedin/", template_name ='blog/account/registration.html')
    else:
        # Отображение страницы с ошибкой
        return HttpResponseRedirect("/account/invalid/", template_name ='blog/account/registration.html')



def logout(request):
    auth.logout(request)
    # Перенаправление на страницу.
    return HttpResponseRedirect("/account/loggedout/", template_name ='blog/account/registration.html')