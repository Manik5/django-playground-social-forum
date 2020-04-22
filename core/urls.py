from django.urls import path

from . import views


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("user/<username>/", views.userProfileView, name="user_profile"),
]
