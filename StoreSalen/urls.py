from django.urls import path # type: ignore
from . import views
from django.contrib.auth import views as auth_views # type: ignore
from django.contrib.auth import views as auth_views # type: ignore

urlpatterns = [
    #path("login/", auth_views.LoginView.as_view(), name="login"),
    #path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('', views.dashboard, name="dashboard"),
]