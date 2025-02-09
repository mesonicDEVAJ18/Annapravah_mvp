from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import DonationForm, RequestForm
from .models import Donation, Request
import logging
from datetime import datetime
from geopy.distance import geodesic

logger = logging.getLogger(__name__)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        print(f"🛠 DEBUG: Received POST data: {request.POST}")
        username = request.POST.get('username')
        password = request.POST.get('password')
        logger.info(f"📝 Received login attempt for username: {username}")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            logger.info(f"✅ Login successful for user: {username}")
            return redirect('home')
        else:
            logger.warning(f"❌ Login failed for user: {username}")
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        print(f"🛠 DEBUG: Received POST data: {request.POST}")
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        logger.info(f"📝 Received signup attempt for username: {username}")

        if User.objects.filter(username=username).exists():
            logger.warning(f"❌ Signup failed: Username '{username}' already exists")
            messages.error(request, 'Username is already taken.')
        elif password1 != password2:
            logger.warning(f"❌ Signup failed for {username}: Passwords do not match")
            messages.error(request, 'Passwords do not match.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            logger.info(f"✅ Signup successful for user: {username}")
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')

    return render(request, 'signup.html')


def logout_view(request):
    if request.user.is_authenticated:
        logger.info(f"🔓 User logged out: {request.user.username}")
        logout(request)
    return redirect('login')

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

def compute_match_score(donation, req, weights):
    today = datetime.today().date()
    expiry_diff = abs((donation.expiry_date - today).days)
    quantity_diff = abs(donation.quantity - req.quantity)
    
    donation_coords = (float(donation.latitude), float(donation.longitude))
    request_coords = (float(req.latitude), float(req.longitude))
    distance = geodesic(donation_coords, request_coords).km

    score = weights['expiry'] * expiry_diff + weights['quantity'] * quantity_diff + weights['distance'] * distance
    return score

def find_best_matches(requests, donations):
    # Define weights for each attribute. Adjust as needed.
    weights = {
        'expiry': 0.5,    # weight for expiry difference (days)
        'quantity': 0.3,  # weight for quantity difference (kg)
        'distance': 0.2   # weight for geographic distance (km)
    }
    matches = []
    
    for req in requests:
        # Only consider donations with the same food type.
        matching_donations = [don for don in donations if don.food_type == req.food_type]
        if not matching_donations:
            continue
        
        scored_donations = []
        for don in matching_donations:
            score = compute_match_score(don, req, weights)
            scored_donations.append((don, score))
        
        # Sort donations by score (lowest first)
        scored_donations.sort(key=lambda item: item[1])
        best_donation, best_score = scored_donations[0]
        matches.append((req, best_donation, best_score))
    
    # Optionally, sort all matches by the score if you want an overall priority order.
    matches.sort(key=lambda item: item[2])
    return matches

def logistics(request):
    requests = Request.objects.all()
    donations = Donation.objects.all()
    matches = find_best_matches(requests, donations)
    context = {
        'matches': matches
    }
    return render(request, 'logistics.html', context)

def navigate(request, req_id, don_id):
    # Retrieve the Request and Donation objects or return 404 if not found.
    req_obj = get_object_or_404(Request, id=req_id)
    don_obj = get_object_or_404(Donation, id=don_id)
    
    # Optionally, calculate the distance between the donation and request.
    # Here we treat donation's location as the pickup point and request's location as the delivery point.
    if (req_obj.latitude is not None and req_obj.longitude is not None and
        don_obj.latitude is not None and don_obj.longitude is not None):
        req_coords = (float(req_obj.latitude), float(req_obj.longitude))
        don_coords = (float(don_obj.latitude), float(don_obj.longitude))
        distance = geodesic(don_coords, req_coords).km
    else:
        distance = None
    
    context = {
        'request_obj': req_obj,
        'donation_obj': don_obj,
        'distance': distance,  # If you need to display this on the page as well.
    }
    
    return render(request, 'navigate.html', context)

def network(request):
    return render(request, 'network.html')

def deliver_happiness(request):
    return render(request, 'deliver_happiness.html')

def partner_ngo(request):
    return render(request, 'partner_ngo.html')