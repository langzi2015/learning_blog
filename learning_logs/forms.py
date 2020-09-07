from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'text']
        labels = {'title': '标题', 'text': '笔记'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
