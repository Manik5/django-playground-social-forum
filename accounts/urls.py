from django.urls import path
from .views import registrationView

urlpatterns = [
  path('registration/', registrationView, name="registration_view")
]
