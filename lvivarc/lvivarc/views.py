from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from architecture.models import ArchitectureGroup

def homepage(request: HttpRequest) -> HttpResponse:
    groups = ArchitectureGroup.objects.all()
    return render(request, 'index.html', context={'groups': groups})