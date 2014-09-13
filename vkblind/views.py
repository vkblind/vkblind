# coding: utf-8

from annoying.decorators import render_to
from django.contrib.auth import logout as logout_user
from django.contrib.auth.decorators import login_required
from django.shortcuts import resolve_url, redirect

@login_required
@render_to('index.html')
def index(request):
    return {}


@render_to('accounts/login.html')
def login(request):
    return {}


def logout(request):
    logout_user(request)
    return redirect(resolve_url('home'))
