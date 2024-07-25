from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'include/about.html')


def portfolio(request):
    return render(request, 'include/portfolio.html')


def contact(request):
    return render(request, 'include/contact.html')