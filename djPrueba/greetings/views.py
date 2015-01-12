from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse, HttpRequest 


# Create your views here.
def default(request):
    return render(request,'index.html')
