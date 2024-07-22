from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
#-------------------------------------work-------------------------------
app_name = 'work'
urlpatterns = [
    path('task/', views.task, name='task'),
    path('home/', views.home, name='home'),
    path('features/', views.features, name='features'),
    path('team/', views.team, name='team'),
    path('faq/', views.faq, name='faq'),
    path('pricing-page/', views.pricing_page, name='pricing-page'),
    path('payment-page/', views.payment_page, name='payment-page'),
    path('checkout-page/', views.checkout_page, name='checkout-page'),
    path('help-center/', views.help_center, name='help-center-landing'),
    path('contact/', views.contact, name='contact'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.register, name='register'),
]