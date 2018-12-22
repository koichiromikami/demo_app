from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("input_form", views.input_form, name="input_form"),
    path("result", views.result, name="result"),
    path('history', views.history, name='history'),
    path("signup", views.signup, name="signup"),
    path("info", views.info, name="info")
]
