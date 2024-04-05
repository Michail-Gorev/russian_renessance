from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from registrationPage.forms import CustomerRegistrationForm


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    form = CustomerRegistrationForm()
    data = {
        'form': form
    }
    get_client_ip(request)
    return render(request, "registration/registration.html", data)


class RegisterView(FormView):
    form_class = CustomerRegistrationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def validate_username(request):
    username = request.GET.get('username', None)
    response = {
        'taken': User.objects.filter(username__exact=username).exists()
    }
    return JsonResponse(response)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print('На странице активен пользователь с IP: ' + ip)
    return ip


def validate_email(request):
    email = request.GET.get('email', None)
    response = {
        'taken': User.objects.filter(email__exact=email).exists()
    }
    return JsonResponse(response)
