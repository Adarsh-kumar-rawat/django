from django.http import HttpResponse
from django.shortcuts import render

def home(req):
    #return HttpResponse("ATMKBFJ")
    return render(req,'index.html')

def about(req):
    return HttpResponse("dadi")

def contact(req):
    return HttpResponse("ok yaal")

