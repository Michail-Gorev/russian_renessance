from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from loginPage.views import profile_view

urlpatterns = [
    path('profile', profile_view, name='profile'),
]