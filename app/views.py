from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def hello(view):
    text = """<h1> this is mys django framework!</h1>"""
    return HttpResponse(text)

def home(view):
    text = """<h1> this is my home django framework!</h1>"""
    return HttpResponse(text)    
