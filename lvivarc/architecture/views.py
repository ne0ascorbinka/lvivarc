from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import ArchitectureGroup

# Create your views here.
def group_page(request: HttpRequest, slug: str) -> HttpResponse:
    group = get_object_or_404(ArchitectureGroup, slug=slug)
    return render(request, 'group.html', context={"group": group})