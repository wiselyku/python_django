from django import forms
from hello.models import LogMessage, ToDoList

class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",)   # NOTE: the trailing comma is required

class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ("taskName","taskContent",)

        