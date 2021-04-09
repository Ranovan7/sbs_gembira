from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login")
def index(request):
    return render(request, 'main/index.html', {})


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('login')


class LoginView(View):

    def get(self, request):
        return render(request, 'main/login.html', {})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Success')
            return redirect('index')
        else:
            messages.error(request, 'Login Failed')
            return render(request, 'main/login.html', {})


def forbidden(request):
    return render(request, 'main/403.html', {})
