from django.shortcuts import render,redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')