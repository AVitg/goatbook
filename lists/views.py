from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request): 
    page="<html> <title>To-Do lists</title> <body> Hello World</body></html>" 
    return HttpResponse(page)