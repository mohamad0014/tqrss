from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "main.html")


def loginPage(request):
    context = {}
    return render(request, 'login.html', context)
    # if request.user.is_authenticated:
    #     return redirect('/')
    # else:
    #     if request.method == 'POST':
    #         username = request.POST.get('username')
    #         password = request.POST.get('password')

    #         user = authenticate(request, username=username, password=password)

    #         if user is not None:
    #             login(request, user)
    #             return redirect('/')
    #         else:
    #             messages.info(request, 'Username OR password is incorrect')

    #     context = {}
    #     return render(request, 'login.html', context)


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


def logoutUser(request):
    logout(request)
    return redirect('login')


def user_list(request):
    return render(request, "users/list.html")


def add_user(request):
    return render(request, "users/add.html")
