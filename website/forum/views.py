from django.shortcuts import render, redirect
from .models import Section, Thread, Post
from django.http import Http404
from django.contrib.auth import login, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import CommentForm

# Create your views here.

def index(request):
    sections = Section.objects.all()
    threads = Thread.objects.all()
    context = {
        'sections' : sections,
        'threads': threads,
    }
    return render(request, 'forum/index.html', context)

def thread(request, thread_id):
    try:
        thread = Thread.objects.get(id=thread_id)
    except Section.DoesNotExist:
        raise Http404("Taki temat nie istnieje")
    posts = Post.objects.filter(thread=thread)
    return render(request, 'forum/thread.html', {'thread' : thread, 'posts': posts})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('../')
    else:
        form = UserCreationForm()
    return render(request, 'forum/register.html', {'form': form})

def post(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = CommentForm()
    return render(request, 'index.html', {'form': form})