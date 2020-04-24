from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from forum.models import Discussion, Post, Section
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

def search(request):
    if "q" in request.GET:
        querystring = request.GET.get("q")
        print(querystring)
        if len(querystring) == 0:
          return redirect("/search/")
        discussions = Discussion.objects.filter(title__icontains=querystring)
        posts = Post.objects.filter(content__icontains=querystring)
        users = User.objects.filter(username__icontains=querystring)
        context = {"discussions": discussions, "posts": posts, "users": users}
        return render(request, 'core/search.html', context)
    else:
        return render(request, 'core/search.html')
