from django.urls import path

from .views import view_sample

urlpatterns = [
    path("", view_sample),
]
