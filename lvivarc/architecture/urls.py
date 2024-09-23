from django.urls import path
from .views import group_page

urlpatterns = [
    path("<slug:slug>", group_page, name="group_detail")
]
