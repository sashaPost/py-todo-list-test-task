from django import forms
from django.conf import settings

from .models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    deadline = forms.DateTimeField(
        input_formats=settings.DATETIME_INPUT_FORMATS,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "YYYY-MM-DD 23:59:59"}),
    )

    class Meta:
        model = Task
        fields = "__all__"