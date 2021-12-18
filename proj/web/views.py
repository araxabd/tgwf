from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from random import choice
from string import ascii_letters, digits
from .models import Token
from .forms import RegisterForm

random_string = lambda L: ''.join(choice(ascii_letters + digits) for i in range(L))

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            this_user = form.save()
            login(request, this_user)
            Token.objects.create(user=this_user, key=random_string(40))
            return redirect('web:home')
    form = RegisterForm()
    return render(request, 'register.html', {'form': form})

#TODO: login without register view

def home_page(request):
    this_token = Token.objects.get(user=request.user)
    return JsonResponse(
        {
            'token': this_token.key,
        }
    )
