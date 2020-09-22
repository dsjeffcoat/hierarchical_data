from django import forms
from .models import Genre
from mptt.forms import TreeNodeChoiceField

class CreateGenreForm(forms.Form):
    name = forms.CharField(max_length=100)
    parent = TreeNodeChoiceField(queryset=Genre.objects.all())