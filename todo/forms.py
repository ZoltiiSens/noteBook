from django.forms import ModelForm
from .models import Week, Todo


class TodoWeekForm(ModelForm):
    class Meta:
        model = Week
        fields = ['title']


class TodoTodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'md', 'td', 'wd', 'th', 'fr', 'st', 'sd']

