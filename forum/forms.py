from django import forms
from .models import Discussion

class DiscussionModelForm(forms.ModelForm):
    content = forms.CharField(
        widget = forms.Textarea(attrs={"placeholder": "What would you like to talk about?"}),
        max_length=4000, label = "First Message")

    class Meta:
        model = Discussion
        fields = ['title', 'content']
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Title Discussion"})}
