from django.shortcuts import render
from django.views.generic import DetailView

from toursPage.models import Tour, Visual, TourDetail


# Create your views here.
def tours(request):
    tours = Tour.objects.all()
    return render(request, 'tours.html', {'tours': tours})


def vision(request):
    visuals = Visual.objects.order_by('index').all()
    return render(request, 'vision.html', {'visuals': visuals})


class TourDetailsView(DetailView):
    model = TourDetail
    template_name = 'tour_details.html'
    context_object_name = 'tour_details'

