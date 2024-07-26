from django.views.decorators.cache import cache_page
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


@cache_page(60 * 15)
def about(request):
    return render(request, "personal/about.html")


def portfolio(request):
    return render(request, "personal/portfolio.html")


def contact(request):
    my_dict = {'Email': 'bbc@gmail.com', 
               'Linkdln': 'shahabaj khan', 
               'Github': 'babagithub.com'
               }
    return render(request, "personal/contact.html", context= {'my_dict':my_dict})
