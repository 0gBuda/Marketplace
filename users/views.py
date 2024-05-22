from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from goods.models import Products
from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm
from users.models import User


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'users/registration.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))

    else:
        form = ProfileForm(instance=request.user)

    context = {
        'form': form
    }
    return render(request, 'users/profile.html', context)


def user_products(request):
    user = request.user
    products = Products.objects.filter(user=user)

    context = {
        'user': user,
        'products': products
    }
    return render(request, 'users/user_products.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('users:login'))


def user_cart(request):
    return render(request, 'users/user-cart.html')
