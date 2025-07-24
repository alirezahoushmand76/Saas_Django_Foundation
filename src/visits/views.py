from django.shortcuts import render
from django.http import HttpResponse
from .models import PageVisit

# Create your views here.

def page_visit_view(request):
    PageVisit.objects.create(path='/', subdomain='www')
    return HttpResponse("Hello")