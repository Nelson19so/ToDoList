from django import forms
from .models import TodoItems

# form

class TodoItemsForm(forms.ModelForm):
  class Meta:
    model = TodoItems
    fields = ('todo', 'description', 'day')