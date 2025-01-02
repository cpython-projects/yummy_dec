from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout

from account.forms import LoginForm, RegistrationForm


class UserLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm

    def get_success_url(self):
        return self.request.GET.get('next', '/')


class UserRegistrationView(CreateView):
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


def logout_view(request):
    logout(request)
    return redirect('home')
