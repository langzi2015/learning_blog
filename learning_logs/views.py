from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.shortcuts import render

from .forms import TopicForm, EntryForm
from .models import Topic, Entry


# Create your views here.
def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """学习笔记的主题页"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """单个主题的所有条目"""
    topic = Topic.objects.get(id=topic_id)
    if request.user != topic.owner:
        return Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries, 'isError': 0}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """添加主题"""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def edit_topic(request, topic_id):
    """编辑主题"""
    topic=Topic.objects.get(id=topic_id)
    if request.user != topic.owner:
        return Http404
    if request.method != 'POST':
        form = TopicForm(instance=topic)
    else:
        form = TopicForm(instance=topic, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_topic.html', context)


@login_required
def delete_topic(request, topic_id):
    """删除主题"""
    topic=Topic.objects.get(id=topic_id)
    if request.user != topic.owner:
        return Http404
    if request.method == 'POST':
        topic.delete()
    return HttpResponseRedirect(reverse('learning_logs:topics'))



@login_required
def new_entry(request, topic_id):
    """为某一个主题添加条目"""
    topic = Topic.objects.get(id=topic_id)
    if request.user != topic.owner:
        return Http404
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """修改特定条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.user != topic.owner:
        return Http404
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    context = {'topic': topic, 'entry': entry, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


@login_required
def delete_entry(request, entry_id):
    """删除条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.user != topic.owner:
        return Http404
    if request.method == 'POST':
        entry.delete()
    return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))

