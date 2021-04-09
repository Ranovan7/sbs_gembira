from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from database.models import Sales, Users
from apps.utils import role_required


@login_required(login_url="/login")
@role_required("admin")
def index(request):
    sales = Sales.objects.order_by('id').all()
    return render(request, 'sales/index.html', {"sales": sales})


class SalesUserView(View):

    @method_decorator(login_required(login_url="/login"))
    @method_decorator(role_required("admin"))
    def get(self, request, sales_id):
        sales = Sales.objects.get(id=sales_id)
        return render(request, 'sales/sales_user.html', {"sales": sales})

    @method_decorator(login_required(login_url="/login"))
    @method_decorator(role_required("admin"))
    def post(self, request, sales_id):
        sales = Sales.objects.get(id=sales_id)

        if not sales:
            messages.error(request, f"Data sales tidak ditemukan")
            return redirect("sales")

        username = request.POST['username']
        password = request.POST['password']

        new_obj = Users(
            username=username,
            role=2
        )
        new_obj.set_password(password)
        new_obj.save()

        sales.user_id = new_obj.id
        sales.save()

        messages.success(request, f"User untuk sales {sales.nama} berhasil ditambahkan")
        return redirect("sales")
