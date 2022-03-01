from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from app.models import CreateUserForm
from tqrss.core.develop_v4 import *
import threading
from os import path


def index(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    return render(request, "main.html")


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)


def generate_plan(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    if request.method == 'POST':
        print('generating plan...')
        t = threading.Thread(target=generate, args=(), kwargs={})
        t.setDaemon(True)
        t.start()
        return render(request, "generate-plan.html", {'generating': True, 'Horizon': request.POST.get('horizon', '')})
    else:
        return render(request, "generate-plan.html", {'generating': False})


def generate_plan_status(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    if(path.exists('logs/Error_log.txt')):
        with open('logs/Error_log.txt') as f:
            errors = f.readlines()
        return JsonResponse({'errors': errors})


def review_plan(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    return render(request, "review-plan.html")


def plans_list(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    return render(request, "plans-list.html")


def compare_plan(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    return render(request, "compare-plan.html")


def release_plan(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    return render(request, "release-plan.html")


def logoutUser(request):
    logout(request)
    return redirect('login')


def user_list(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    filter_term = ''
    if request.method == 'POST':
        filter_term = request.POST.get('filter_term')
        users = User.objects.filter(Q(username__contains=filter_term) | Q(
            first_name__contains=filter_term) | Q(last_name__contains=filter_term))
    else:
        users = User.objects.all()
    context = {'users': users, 'filter_term': filter_term}
    return render(request, "users/list.html", context)


def add_user(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    userinstance = None
    if request.method == 'POST':
        print('POST Add User')
        form = CreateUserForm(request.POST)
        if form.is_valid():
            print('form.is_valid')
            userinstance = form.save()
            form = CreateUserForm()
        else:
            print('errors')
    else:
        form = CreateUserForm()

    context = {'form': form, 'newuser': userinstance}
    return render(request, "users/add.html", context)
