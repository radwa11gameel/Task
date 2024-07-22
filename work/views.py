# views.py
from django.shortcuts import render,redirect
from .models import Task, Home, Feature, TeamMember, FAQ, Contact, PricingPage, PaymentPage, CheckoutPage, HelpCenter
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
def task(request):
    tasks = Task.objects.all()
    return render(request, 'base.html', {'tasks': tasks})

def home(request):
    home_content = Home.objects.all()
    return render(request, 'landing-page.html', {'home_content': home_content})

def features(request):
    features = Feature.objects.all()
    return render(request, 'features.html', {'features': features})

def team(request):
    team_members = TeamMember.objects.all()
    return render(request, 'help-center-landing.html', {'team_members': team_members})

def faq(request):
    faqs = FAQ.objects.all()
    return render(request, 'faq.html', {'faqs': faqs})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        Contact.objects.create(name=name, email=email, message=message)
    return render(request, 'contact.html')

def pricing_page(request):
    pricing_plans = PricingPage.objects.all()
    return render(request, 'pricing-page.html', {'pricing_plans': pricing_plans})

def payment_page(request):
    payment_methods = PaymentPage.objects.all()
    return render(request, 'payment-page.html', {'payment_methods': payment_methods})

def checkout_page(request):
    checkout_items = CheckoutPage.objects.all()
    return render(request, 'checkout-page.html', {'checkout_items': checkout_items})

def help_center(request):
    help_center_content = HelpCenter.objects.all()
    return render(request, 'help-center-landing.html', {'help_center_content': help_center_content})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('base')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})