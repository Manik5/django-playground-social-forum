from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from forum.models import Discussion, Section
from django.views.generic.list import ListView
# Create your views here.

# def homepage(request):
#   return render(request, 'core/homepage.html')


class HomeView(ListView):
    queryset = Section.objects.all()
    template_name = 'core/homepage.html'
    context_object_name = "list_section"


class UserList(LoginRequiredMixin, ListView):
    model = User
    template_name = 'core/users.html'

def userProfileView(request, username):
    user = get_object_or_404(User, username=username)
    discussions_user = Discussion.objects.filter(author_discussion=user).order_by("-pk")
    context = {"user": user, "discussions_user": discussions_user}
    return render(request, 'core/user_profile.html', context)
