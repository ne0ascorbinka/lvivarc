from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def homepage(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')