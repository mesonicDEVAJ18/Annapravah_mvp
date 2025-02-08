from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import DonationForm
from .models import Donation

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
    donations = Donation.objects.all()
    return render(request, 'donor_dashboard.html', {'donations': donations})

def donation_add(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            # Save the donation
            donation = form.save(commit=False)
            donation.save()  # Save the donation to the database
            messages.success(request, 'Donation submitted successfully!')
            return redirect('donor_dashboard')  # Redirect to the same page after submission
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = DonationForm()

    # Fetch past donations to display in the "Past Donations" tab
    past_donations = Donation.objects.all().order_by('-created_at')

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
    return render(request, 'request_food.html')

def navigate(request):
    return render(request, 'navigate.html')

def network(request):
    return render(request, 'network.html')

def deliver_happiness(request):
    return render(request, 'deliver_happiness.html')

def partner_ngo(request):
    return render(request, 'partner_ngo.html')
