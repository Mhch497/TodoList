from django.core.mail.backends import console

from .models import *
from django.forms import ModelForm, TextInput, Select, BooleanField, NumberInput
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField


class TaskForm(ModelForm):
    class Meta:
        model = Task
        categories = Category.objects.all()
        category = [cat for cat in categories]
        fields = ["task", "content", "data_todo", "category"]
        widgets = {
            "task": TextInput(attrs={
                'class': 'form-control title',
                'placeholder': 'Что вы хотите сегодня сделать?'
            }),
            "content": TextInput(attrs={
                'class': 'form-control content',
                'placeholder': 'Добавьте описание, чтобы ничего не забыть :)'
            }),
            "data_todo": NumberInput(attrs={
                'type':'date'
            }),
            "category": Select(attrs={
                'class': 'form-control cat',
                'title': 'Выберите категорию'
            }, choices=category),
        }


class CatForm(ModelForm):
    class Meta:
        model = Category

        fields = ["name"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control title',
                'placeholder': 'Давайте добавим категорию'
            }),
        }

