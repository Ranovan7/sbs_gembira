from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='sales'),
    path('<int:sales_id>/add_user', views.SalesUserView.as_view(), name='sales-user'),
]
