from django import forms
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model =  Post
        fields = ('__all__')

class CommentForm(forms.ModelForm):
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'rows':4
    }))
    class Meta:
        model =  Comments
        fields = ('content',)