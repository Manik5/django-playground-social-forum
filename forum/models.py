from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import math
# Create your models here.

class Section(models.Model):
  # sections divide the app by categories of discussions.
  # Each section contains many discussions
  # Created by the admin
  name_section = models.CharField(max_length=80)
  description = models.CharField(max_length=150, blank=True, null=True)
  logo_section = models.ImageField(blank=True, null=True)

  def __str__(self):
    return self.name_section

  def get_absolute_url(self):
    return reverse("section_view", kwargs={"pk": self.pk})


  def get_last_discussions(self):
    return Discussion.objects.filter(belong_section=self).order_by("-creation_date")[:2]

  def get_number_of_posts_in_section(self):
    return Post.objects.filter(discussion__belong_section=self).count()

class Discussion(models.Model):
  title = models.CharField(max_length=120)
  creation_date = models.DateTimeField(auto_now_add=True)
  author_discussion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="discussions")
  belong_section = models.ForeignKey(Section, on_delete=models.CASCADE)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse("visualize_discussion", kwargs={"pk": self.pk})

  def get_n_pages(self):
    posts_discussion = self.post_set.count()
    n_pages = math.ceil(posts_discussion / 5)
    return n_pages

class Post(models.Model):
  author_post = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
  content = models.TextField()
  creation_date = models.DateTimeField(auto_now_add=True)
  discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)

  def __str__(self):
    return self.author_post.username
