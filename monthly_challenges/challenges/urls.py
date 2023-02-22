"""Urls."""
from django.urls import path

from .views import index, monthly_challenge, monthly_challenge_by_idx

urlpatterns = [
    path("<int:month>", monthly_challenge_by_idx),
    path("<str:month>", monthly_challenge, name="month-challenge"),
    path("", index, name="index"),
]
