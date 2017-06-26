from django import forms
from api.models import Tag


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ('name',)