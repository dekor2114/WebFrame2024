from django.shortcuts import render

# Create your views here.
def main(request):
    return render(
        request,
        'exam2/main.html',
    )
def carsale(request):
    #posts = CarTrade2.objects.all()
    return render(
        request,
        'exam2/carsale.html',
       
    )