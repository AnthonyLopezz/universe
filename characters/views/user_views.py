from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        _username = request.POST['username']
        _password = request.POST['password']
        user = authenticate(request, username=_username, password=_password)

        if user:
            login(request, user)
            return redirect('characters')
        else:
            return render(request, 'users\\login.html', {'error': 'el usuario no existe.'})

    return render(request, 'users\\login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')