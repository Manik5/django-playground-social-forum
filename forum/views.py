from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
# Create your views here.
from .mixins import StaffMixing
from .models import Section

class CreateSection(StaffMixing, CreateView):
    model = Section
    fields = "__all__"
    template_name = "forum/create_section.html"
    success_url = "/"

def visualizeSection(request, pk):
    section = get_object_or_404(Section, pk=pk)
    context = {"section": section}
    return render(request, "forum/single_section.html", context)

def createDiscussion(request, pk):
    section = get_object_or_404(Section, pk=pk)

