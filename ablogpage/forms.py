from django import forms
from .models import Post


class Postform(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Post
        fields='__all__'