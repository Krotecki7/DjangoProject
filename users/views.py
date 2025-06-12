from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.contrib.auth import login
import os
from dotenv import load_dotenv
from .forms import CustomUserCreationForm, CustomAuthenticationForm


class CustomLoginView(LoginView):
    template_name = "users/login.html"
    form_class = CustomAuthenticationForm
    success_url = reverse_lazy("catalog:product_list")


class CustomRegisterView(FormView):
    template_name = "users/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в магазин комьютерных игры - "SkyStore"'
        message = "Спасибо, что присоединились к нам!"
        from_email = os.getenv("EMAIL_HOST_USER")
        recipient_list = [
            user_email,
        ]
        send_mail(subject, message, from_email, recipient_list)


class CustomLogoutView(LogoutView):
    template_name = "users/logout.html"
    next_page = reverse_lazy("users:logout")


class NotAuthView(TemplateView):
    template_name = "users/not_auth.html"
