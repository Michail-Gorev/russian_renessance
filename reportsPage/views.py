from django.contrib.auth.models import User
from django.shortcuts import render

from .forms import FeedbackForm
from .models import Feedback


def feedback_form(request):
    reports = Feedback.objects.all()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FeedbackForm()
    data = {
        'form': form,
        'reports': reports,
    }
    return render(request, 'reports.html', data)