from django.contrib import admin

from toursPage.models import Tour, Visual, TourDetail, Category

# Register your models here.
admin.site.register(Tour)
admin.site.register(Category)
admin.site.register(Visual)
admin.site.register(TourDetail)
