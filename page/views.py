from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def community(request):
    return render(request, 'community.html')

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

