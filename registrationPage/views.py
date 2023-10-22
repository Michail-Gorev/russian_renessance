from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy

from registrationPage.forms import CustomerForm, CustomerRegistrationForm


# Create your views here.
def registration_and_authentication(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
    form = CustomerRegistrationForm()
    data = {
        'form': form
    }
    get_client_ip(request)
    return render(request, "registration_and_authentication.html", data)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print('На странице активен пользователь с IP: ' + ip)
    return ip


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('home')



