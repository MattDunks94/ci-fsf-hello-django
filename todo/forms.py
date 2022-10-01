from django import forms
from .models import Item

# Creates form for adding item with 2 fields: name, done.
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'done']