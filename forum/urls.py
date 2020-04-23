from django.urls import path
from . import views

urlpatterns = [
  path('new-section/', views.CreateSection.as_view(), name="create_section")
]
