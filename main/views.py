from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def LandingPage(response):
    context = {}
    return render(response, "main/landingpage.html", context)