from django.shortcuts import render

from django.http import HttpResponse

def welcome(request):
    return render(request, "welcome.html")

def product(request):
    return render(request, "product.html")

def contact(request):
    return render(request, "contact.html")
