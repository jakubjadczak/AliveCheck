from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver
from .forms import SignUpForm


@receiver(user_logged_out)
def on_user_logged_out(sender, request, **kwargs):
    messages.info(request, "You have been logged out successfully.")


class MyLoginView(LoginView):
    template_name = "users/login.html"
    redirect_authenticated_user = True

    def form_valid(self, form):
        messages.success(self.request, "Successfully logged in!")
        return super().form_valid(form)


class MyLogoutView(LogoutView):
    next_page = reverse_lazy("main:home")


class MyRegisterView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("users:login")
    template_name = "users/register.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Successfully registered!")
        return response
