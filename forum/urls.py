from django.urls import path
from . import views

urlpatterns = [
    path('new-section/', views.CreateSection.as_view(), name="create_section"),
    path('section/<int:pk>', views.visualizeSection, name="section_view"),
    path('section/<int:pk>/create-discussion',
         views.createDiscussion,
         name="create_discussion"),
    path('discussion/<int:pk>',
         views.visualizeDiscussion,
         name="visualize_discussion"),
    path('discussion/<int:pk>/response',
         views.addResponse,
         name="response_discussion"),
    path('discussion/<int:pk>/cancel-post/<int:pk>/',
         views.CancelPost.as_view(),
         name="cancel_post"),
]
