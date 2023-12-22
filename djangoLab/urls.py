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
import reportsPage.views
import toursPage
from homePage import views
from loginPage.views import profile_view
from toursPage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homePage.views.home),
    path('contacts/', homePage.views.contacts),
    path('reports/', reportsPage.views.feedback_form),
    path('', homePage.views.home, name='home'),
    path('/tours/', toursPage.views.tours, name='tours'),
    path('tours/<int:pk>', toursPage.views.TourDetailsView.as_view(), name='tour_details'),
    path('register', registrationPage.views.RegisterView.as_view(), name='register'),
    path('about/', homePage.views.about, name='about'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('profile', profile_view, name="profile"),
    path('tours/category/<int:cat_id>/', toursPage.views.show_category, name='category'),
    path('<int:id>/delete/', toursPage.views.tourDeleteView.as_view(), name='tour_delete'),
    path('ajax/validate_username', registrationPage.views.validate_username, name='validate_username'),
    path('ajax/validate_email', registrationPage.views.validate_email, name='validate_email'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
