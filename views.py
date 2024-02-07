from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'harry/index.html')


def biography(request):
    return render(request, 'harry/biography.html')

def event(request):
    return render(request, 'harry/event.html')

def socialcampagion(request):
    return render(request, 'harry/socialcampagion.html')

def contactus(request):
    return render(request, 'harry/contactus.html')