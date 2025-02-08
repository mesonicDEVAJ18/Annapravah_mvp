from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to homepage after login
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            return redirect('login')  # Redirect to login page after signup

    return render(request, 'signup.html')


def home(request):
    return render(request, 'home.html')

def donor_dashboard(request):
    return render(request, 'donor_dashboard.html')

def logistics(request):
    return render(request, 'logistics.html')

def admin_panel(request):
    return render(request, 'admin_panel.html')

def request_food(request):
    return render(request, 'request_food.html')

def navigate(request):
    return render(request, 'navigate.html')

def network(request):
    return render(request, 'network.html')

def deliver_happiness(request):
    return render(request, 'deliver_happiness.html')

def partner_ngo(request):
    return render(request, 'partner_ngo.html')
