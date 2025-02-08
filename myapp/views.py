from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import DonationForm, RequestForm
from .models import Donation, Request

def login_view(request):
    if request.method == "POST":
        print(f"📝 Received login attempt with data: {request.POST}")  # Debugging print
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            print(f"✅ Login successful for user: {username}")  # Debugging print
            login(request, user)
            return redirect('home')
        else:
            print(f"❌ Login failed for user: {username}")  # Debugging print
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

def signup_view(request):
    if request.method == "POST":
        print(f"📝 Received signup attempt with data: {request.POST}")  # Debugging print
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            print(f"✅ Signup successful for user: {username}")  # Debugging print
            return redirect('login')
        else:
            print(f"❌ Signup failed: Passwords do not match")  # Debugging print
            messages.error(request, 'Passwords do not match.')

    return render(request, 'signup.html')

def home(request):
    return render(request, 'home.html')

def donor_dashboard(request):
    donations = Donation.objects.all()
    print(f"📊 Fetching all donations: {donations}")  # Debugging print
    return render(request, 'donor_dashboard.html', {'donations': donations})

def donation_add(request):
    if request.method == 'POST':
        print(f"📝 Received donation submission with data: {request.POST}")  # Debugging print
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save()
            print(f"✅ Donation saved: {donation}")  # Debugging print
            messages.success(request, 'Donation submitted successfully!')
            return redirect('donor_dashboard')
        else:
            print(f"❌ Donation form errors: {form.errors}")  # Debugging print
            messages.error(request, 'Please correct the errors below.')
    else:
        form = DonationForm()

    past_donations = Donation.objects.all().order_by('-created_at')
    print(f"📊 Fetching past donations: {past_donations}")  # Debugging print

    context = {
        'form': form,
        'donations': past_donations,
    }
    return render(request, 'donor_dashboard.html', context)

def logistics(request):
    return render(request, 'logistics.html')

def admin_panel(request):
    return render(request, 'admin_panel.html')

def request_food(request):
    requests = Request.objects.all()
    print(f"📊 Fetching all requests: {requests}")  # Debugging print
    return render(request, 'request_food.html', {'requests': requests})

def request_add(request):
    if request.method == 'POST':
        print(f"📝 Received request submission with data: {request.POST}")  # Debugging print
        form = RequestForm(request.POST)
        if form.is_valid():
            request_obj = form.save()
            print(f"✅ Request saved: {request_obj}")  # Debugging print
            messages.success(request, 'Request submitted successfully!')
            return redirect('request_food')
        else:
            print(f"❌ Request form errors: {form.errors}")  # Debugging print
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RequestForm()

    past_requests = Request.objects.all().order_by('-created_at')
    print(f"📊 Fetching past requests: {past_requests}")  # Debugging print

    context = {
        'form': form,
        'requests': past_requests,
    }
    return render(request, 'request_food.html', context)

def navigate(request):
    return render(request, 'navigate.html')

def network(request):
    return render(request, 'network.html')

def deliver_happiness(request):
    return render(request, 'deliver_happiness.html')

def partner_ngo(request):
    return render(request, 'partner_ngo.html')