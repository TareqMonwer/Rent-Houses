from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth import logout as auth_logout

from contacts.models import Contact


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    auth_logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        # password match
        if password != password2:
            messages.error(request, 'Password didn\'t match!')
            return redirect('register')
        else:
            if User.objects.filter(username=username):
                messages.error(request, 'Username not available!')
                return redirect('register')
            elif User.objects.filter(email=email):
                messages.error(request, 'Email already registered!')
                return redirect('register')
            else:
                User.objects.create_user(
                    username=username,
                    first_name=fname,
                    last_name=lname,
                    password=password2,
                    email=email
                )
                messages.success(request, 'You are registered and you can login now!')
                return redirect('login')
    else:
        return render(request, 'accounts/register.html')


def dashboard(request):
    contacts = Contact.objects.order_by('-contact_date').filter(contact_id=request.user.id)
    return render(request, 'accounts/dashboard.html', {'contacts': contacts, })
