from django.shortcuts import render
from .models import Notice
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def community(request):
    notices = Notice.objects.all()
    return render(request, 'community.html', {'notices': notices})

def story(request):
    return render(request, 'story.html')

def mypage(request):
    return render(request, 'mypage.html')

def profile(request):
    return render(request, 'profile.html')

def wish(request):
    return render(request, 'wish.html')

def record(request):
    return render(request, 'record.html')

def question(request):
    return render(request, 'question.html')

def survey(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    
def login(request):
    return render(request, 'login.html')
