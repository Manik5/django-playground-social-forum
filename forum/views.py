from django.shortcuts import render
from django.views.generic.edit import CreateView
# Create your views here.
from .mixins import StaffMixing
from .models import Section
class CreateSection(StaffMixing, CreateView):
  model = Section
  fields = "__all__"
  template_name = "forum/create_section.html"
  success_url = "/"
