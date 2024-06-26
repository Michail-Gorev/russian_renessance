from django.shortcuts import render

from homePage.forms import UserForm


# Create your views here.
def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
    form = UserForm()
    data = {
        'form': form
    }
    return render(request, 'contacts.html', data)


def about(request):
    return render(request, 'about.html')
