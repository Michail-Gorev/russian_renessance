from django.shortcuts import render
from toursPage.models import Tour


# Create your views here.
def tours(request):
    tours = Tour.objects.all()
    return render(request, 'tours.html', {'tours': tours})
