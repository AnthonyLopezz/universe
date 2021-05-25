from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required
def show(request):
    return render(request, 'home\\home.html')