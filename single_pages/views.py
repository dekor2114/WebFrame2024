from django.shortcuts import render

# Create your views here.

#views.index로 접근하는 친구
def landing(request):
    return render(
        request,
        'single_pages/landing.html',
    )
def about_me(request):
    return render(
        request,
        'single_pages/about_me.html',
    )
