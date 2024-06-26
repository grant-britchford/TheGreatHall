from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
]