from django.shortcuts import render
from .models import Notice
from allauth.socialaccount.models import SocialAccount
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
    # birthday 및 프로필 사진 가져오기 위해
    social_info = SocialAccount.objects.filter(user=request.user)[0].extra_data['kakao_account']
    return render(request, 'profile.html', {'social_info':social_info})

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