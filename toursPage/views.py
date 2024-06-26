from django.views import View
from django.views.generic import DetailView
from django.shortcuts import render, redirect

from djangoLab import settings
from toursPage.models import Tour, Visual, TourDetail, Category


# Create your views here.
def tours(request):
    tours = Tour.objects.all()
    cats = Category.objects.all()
    context = {'tours': tours,
               'cats': cats
               }

    return render(request, 'tours.html', context=context)


class tourDeleteView(View):

    def post(self, request, *args, **kwargs):
        tour_id = kwargs.get('id')
        tour = Tour.objects.get(tour_id=tour_id)
        tour_detail = TourDetail.objects.get(tour_id=tour_id)
        if tour and tour_detail:
            tour.delete()
            tour_detail.delete()
        return redirect('tours')


def show_category(request, cat_id):
    tours_cats = Tour.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    context = {'tours': tours_cats,
               'cats': cats,
               'cat_selected': cat_id
               }
    return render(request, 'tours.html', context=context)


def vision(request):
    visuals = Visual.objects.order_by('index').all()
    return render(request, 'vision.html', {'visuals': visuals})


class TourDetailsView(DetailView):
    model = TourDetail
    template_name = 'tour_details.html'
    context_object_name = 'tour_details'

