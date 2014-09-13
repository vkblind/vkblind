# -*- coding: utf-8 -*

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def index(request):
    return render(request, 'index.html')

def login(request):
     return render(request, 'accounts/login.html')

def logout(request):
    pass
