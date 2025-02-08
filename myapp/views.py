from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def donor_dashboard(request):
    return render(request, 'donor_dashboard.html')

def ai_matching(request):
    return render(request, 'ai_matching.html')

def logistics(request):
    return render(request, 'logistics.html')

def admin_panel(request):
    return render(request, 'admin_panel.html')

def request_food(request):
    return render(request, 'request_food.html')
