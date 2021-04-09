from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from apps.utils import role_required


@login_required(login_url="/login")
def index(request):
    return render(request, 'pesanan/index.html', {})
