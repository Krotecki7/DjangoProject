from django.urls import path, include
from users.apps import UsersConfig
from django.contrib.auth.views import LoginView, LogoutView
from .views import CustomRegisterView, CustomLogoutView, CustomLoginView, NotAuthView

app_name = UsersConfig.name

urlpatterns = [
    path(
        "login/",
        CustomLoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path("logout/", CustomLogoutView.as_view(next_page="users:logout"), name="logout"),
    path("register/", CustomRegisterView.as_view(), name="register"),
    path("not_auth/", NotAuthView.as_view(), name="not_auth"),
]
