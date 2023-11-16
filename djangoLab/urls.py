"""
URL configuration for firstDjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import homePage
import registrationPage.views
import toursPage
from homePage import views
from toursPage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homePage.views.home),
    path('', homePage.views.home),
    path('tours/', toursPage.views.tours),
    path('tours/<int:pk>', toursPage.views.TourDetailsView.as_view(), name='tour_details'),
    path('registration_and_authentication/', registrationPage.views.registration_and_authentication),
    path('about/', homePage.views.about),
    path('accounts', include("django.contrib.auth.urls")),
    path('tours/category/<int:cat_id>/', toursPage.views.show_category, name='category')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
