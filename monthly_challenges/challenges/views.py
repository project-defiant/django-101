# -*- coding: utf-8 -*-
"""Create views here."""
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    """Index page for challenges app.

    Args:
        request (HttpRequest): incoming request

    Returns:
        HttpResponse: response
    """
    print(request)
    return HttpResponse("This works!")
