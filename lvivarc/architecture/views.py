from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import ArchitectureGroup, ArchitectureObject

# Create your views here.
def group_page(request: HttpRequest, slug: str) -> HttpResponse:
    group = get_object_or_404(ArchitectureGroup, slug=slug)
    arc_objects = group.arc_objects.all()
    return render(request, 'group.html', context={"group": group, "places": arc_objects})

def object_page(request: HttpRequest, pk: int, slug) -> HttpResponse:
    arc_object = get_object_or_404(ArchitectureObject, pk=pk)
    return render(request, 'object.html', context={"place": arc_object, "slug": slug})