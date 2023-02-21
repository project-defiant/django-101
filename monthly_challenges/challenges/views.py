# -*- coding: utf-8 -*-
"""Create views here."""
from collections import OrderedDict

from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseRedirect,
)
from django.shortcuts import render
from django.urls import reverse

monthly_challenges = OrderedDict(
    {
        "january": "learn django 20 min by day",
        "february": "start running",
        "march": "start rust development",
        "april": "start scala development",
        "may": "start Cpp development",
        "june": "str",
        "july": "str",
        "august": "str",
        "september": "str",
        "october": "str",
        "november": "str",
        "december": "Str",
    }
)

# Create your views here.


def monthly_challenge(request: HttpRequest, month: str) -> HttpResponse:
    """Month page for challenges app.

    Args:
        request (HttpRequest): incoming request

    Returns:
        HttpResponse: response
    """
    print(request)
    try:
        text = monthly_challenges[month]
        response_data = f"<h1>{text}</h1>"
    except KeyError:
        return HttpResponseNotFound("<h1>Not a month</h1>")
    return HttpResponse(response_data)


def monthly_challenge_by_idx(
    request: HttpRequest, month: int
) -> HttpResponseRedirect:
    """Month page for challenges app redirection.

    Args:
        request (HttpRequest):
        month (int): month idx

    Returns:
        HttpResponseRedirect: redirect
    """
    print(request)
    try:
        redirect_month = list(monthly_challenges.keys())[month - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
    except IndexError:
        return HttpResponseNotFound("<h1>Not a month</h1>")

    return HttpResponseRedirect(redirect_to=redirect_path)


def index(request: HttpRequest) -> HttpResponse:
    """Index page."""
    print(request)
    return HttpResponse(
        "".join(
            [
                f"<h2><a href={reverse('month-challenge', args=[month])}>{month}</h2>"
                for month in monthly_challenges.keys()
            ]
        )
    )
