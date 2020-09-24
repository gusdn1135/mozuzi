"""mozuzi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from page import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('story/', views.story, name='story'),
    path('', views.home, name='home'),
    path('community', views.community, name='community'),
    path('mypage/', views.mypage, name='mypage'),
    path('mypage/profile/', views.profile, name='profile'),
    path('mypage/record/', views.record, name='record'),
    path('mypage/wish/', views.wish, name='wish'),
    path('community/question', views.question, name='question'),
    path('survey', views.survey, name='survey'),
    path('login/', views.login, name='login'),
    
    # login ------------------------------

        # allauth 라이브러리에 소셜 로그인에 대한 urls.py가 이미 정의되어 있으므로
        # 로그인 시도 요청 시 allauth의 urls.py로 이동할 수 있게 한다
    path('accounts/', include('allauth.urls')),
    
    # ------------------------------ login
