from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("calc_volume/", views.calc_volume, name="calc_volume"),
]
