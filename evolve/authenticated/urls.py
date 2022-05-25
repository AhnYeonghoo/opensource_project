from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "authenticated"

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="authenticated/login.html"), name="login"),
    
]
