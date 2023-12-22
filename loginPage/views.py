import profile

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render

from reportsPage.models import Feedback


# Create your views here.

@login_required
def profile_view(request):
    username = User.username
    feedbacks = Feedback.objects.all()
    data = {
        'feedbacks': feedbacks
    }
    return render(request, 'profile.html', data)


