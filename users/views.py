from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import User


class RegisterView(CreateView):
    model = User
    template_name = 'register.html'
    fields = ['username', 'phone_number', 'password']
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])  # Хэшируем пароль
        user.save()
        return super().form_valid(form)


class CustomLoginView(LoginView):
    template_name = 'login.html'


class CustomLogoutView(LogoutView):
    next_page = 'login'
