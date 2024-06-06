from django.shortcuts import render

# Create your views here.


def aboutme(request):  # 전달인자가 있을 때 request
    return render(request, "single_pages/about_me.html")  # 리퀘스트 한번 리턴해주고


def landing(request):
    return render(request, "single_pages/landing.html")
