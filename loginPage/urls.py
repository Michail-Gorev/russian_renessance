from django.urls import path


from loginPage.views import profile_view
app_name = "loginPage"

urlpatterns = [
    path('profile', profile_view, name="profile")
]
