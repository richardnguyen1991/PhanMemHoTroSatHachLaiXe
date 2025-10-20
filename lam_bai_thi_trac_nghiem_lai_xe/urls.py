from django.urls import path

from . import views

app_name = "lam_bai_thi_trac_nghiem_lai_xe"

urlpatterns = [
    path("", views.trang_chu, name="trang_chu"),
]
