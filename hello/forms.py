from django import forms
from .models import Note
class EntryForm(forms.ModelForm):
    class Meta:
        model=Note
        fields=['title','content']
        