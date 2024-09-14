from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Start writing a blog post about your first day of work.",
    "february": "Write a blog post about your first day of school.",
    "march": "Write a blog post about your first day of college.",
    "april": "Write a blog post about your first day of birthday.",
    "may": "Write a blog post about your first day of vacation.",
    "june": "Write a blog post about your first day of school.",
    "july": "Write a blog post about your first day of college.",
    "august": "Write a blog post about your first day of work.",
    "september": "Write a blog post about your first day of work.",
    "october": "Write a blog post about your first day of school.",
    "november": "Write a blog post about your first day of college.",
    "december": "Write a blog post about your first day of birthday.",
}

# Create your views here.


def monthly_challenge_by_number(request, month):
    monthList = list(monthly_challenges.keys())

    if month not in range(1, 13):
        return HttpResponseNotFound("Month not found.")

    redirectMonth = monthList[month - 1]
    redirect_path = reverse("month_challenge", args=[redirectMonth])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Month not found.")
