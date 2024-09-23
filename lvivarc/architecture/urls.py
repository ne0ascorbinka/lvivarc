from django.urls import path
from .views import group_page, object_page

urlpatterns = [
    path("<slug:slug>/<int:pk>/", object_page, name="object_detail"),
    path("<slug:slug>", group_page, name="group_detail"),
]
