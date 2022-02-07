from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "main.html")


def login(request):
    return render(request, "login.html")


def generate_plan(request):
    return render(request, "generate-plan.html")


def review_plan(request):
    return render(request, "review-plan.html")


def plans_list(request):
    return render(request, "plans-list.html")


def compare_plan(request):
    return render(request, "compare-plan.html")


def release_plan(request):
    return render(request, "release-plan.html")
