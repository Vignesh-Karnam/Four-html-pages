from django.shortcuts import render

# Create your views here.
def One(request):
    return render(request,'One.html')

def Two(request):
    return render(request,'Two.html')

def Three(request):
    return render(request,'Three.html')

def Four(request):
    return render(request,'Four.html')