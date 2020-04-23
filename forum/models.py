from django.db import models
from django.contrib.auth.models import User
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

class Discussion(models.Model):
  title = models.CharField(max_length=120)
  data_creation = models.DateTimeField(auto_now_add=True)
  author_discussion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="discussions")
  belong_section = models.ForeignKey(Section, on_delete=models.CASCADE)

  def __str__(self):
    return self.title

class Post(models.Model):
  author_post = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
  content = models.TextField()
  creation_date = models.DateTimeField(auto_now_add=True)
  discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)

  def __str__(self):
    return self.author_post