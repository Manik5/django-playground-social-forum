from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse
from .forms import DiscussionModelForm, PostModelForm
from .mixins import StaffMixing
from .models import Discussion, Post, Section

class CreateSection(StaffMixing, CreateView):
    model = Section
    fields = "__all__"
    template_name = "forum/create_section.html"
    success_url = "/"

def visualizeSection(request, pk):
    section = get_object_or_404(Section, pk=pk)
    discussions_section = Discussion.objects.filter(belong_section=section).order_by("-creation_date")
    context = {"section": section, "discussions": discussions_section}
    return render(request, "forum/single_section.html", context)

@login_required
def createDiscussion(request, pk):
    section = get_object_or_404(Section, pk=pk)
    if request.method == "POST":
      form = DiscussionModelForm(request.POST)
      if form.is_valid():
        discussion = form.save(commit=False)
        discussion.belong_section = section
        discussion.author_discussion = request.user
        discussion.save()
        first_post = Post.objects.create(
          discussion=discussion,
          author_post=request.user,
          content = form.cleaned_data["content"]
          )
        return HttpResponseRedirect(discussion.get_absolute_url())
    else:
      form = DiscussionModelForm()
    context = {"form": form, "section": section}
    return render(request, "forum/create_discussion.html", context)

def visualizeDiscussion(request, pk):
  discussion = get_object_or_404(Discussion, pk=pk)
  posts_discussion = Post.objects.filter(discussion=discussion)

  paginator = Paginator(posts_discussion, 5)
  page = request.GET.get("page")
  posts = paginator.get_page(page)

  form_response = PostModelForm()
  context = {"discussion": discussion,
             "posts_discussion": posts,
             "form_response": form_response
             }
  return render(request, "forum/single_discussion.html", context)

@login_required
def addResponse(request, pk):
  discussion = get_object_or_404(Discussion, pk=pk)
  if request.method == "POST":
    form = PostModelForm(request.POST)
    if form.is_valid():
      form.save(commit=False)
      form.instance.discussion = discussion
      form.instance.author_post = request.user
      form.save()
      url_discussion = reverse("visualize_discussion", kwargs={"pk": pk})
      return HttpResponseRedirect(url_discussion)
  else:
    return HttpResponseBadRequest()
