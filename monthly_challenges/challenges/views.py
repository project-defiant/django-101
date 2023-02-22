# -*- coding: utf-8 -*-
"""Create views here."""
from collections import OrderedDict

from django.http import (
    Http404,
    HttpRequest,
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseRedirect,
)
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse

monthly_challenges = OrderedDict(
    {
        "january": "learn django 20 min by day",
        "february": "start running",
        "march": "start rust development",
        "april": "start scala development",
        "may": "start Cpp development",
        "june": None,
        "july": None,
        "august": None,
        "september": None,
        "october": None,
        "november": None,
        "december": None,
    }
)


def monthly_challenge(request: HttpRequest, month: str) -> HttpResponse:
    """Month page for challenges app."""
    print(request)
    try:
        text = monthly_challenges[month]
        return render(
            request,
            "challenges/challenge.html",
            {"text": text, "month": month.capitalize()},
        )
    except KeyError as exc:
        raise Http404() from exc


def monthly_challenge_by_idx(
    request: HttpRequest, month: int
) -> HttpResponseRedirect:
    """Redirect month index page to month page."""
    print(request)
    try:
        redirect_month = list(monthly_challenges.keys())[month - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_to=redirect_path)
    except IndexError as exc:
        raise Http404() from exc


def index(request: HttpRequest) -> HttpResponse:
    """Index page."""
    return render(
        request,
        "challenges/index.html",
        {"data": list(monthly_challenges.keys())},
    )
