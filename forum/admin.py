from django.contrib import admin
from .models import Discussion, Post, Section
# Register your models here.

class DiscussionModelAdmin(admin.ModelAdmin):
    model = Discussion
    list_display = ["title", "belong_section", "author_discussion"]
    search_fields = ["title", "author_discussion"]
    list_filter = ["belong_section", "creation_date"]

class PostModelAdmin(admin.ModelAdmin):
    model = Post
    list_display = ["author_post", "discussion"]
    search_fields = ["content"]
    list_filter = ["creation_date", "author_post"]


class SectionModelAdmin(admin.ModelAdmin):
    model = Section
    list_display = ["name_section", "description"]


admin.site.register(Discussion, DiscussionModelAdmin)
admin.site.register(Post, PostModelAdmin)
admin.site.register(Section, SectionModelAdmin)
