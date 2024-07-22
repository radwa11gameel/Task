# models.py
from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Home(models.Model):
    
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField()
    image = models.ImageField(upload_to='homepage_images/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    

class Feature(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    detailed_description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='feature_images/', blank=True, null=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(("Name"), max_length=160)
    icon = models.CharField(("Icon"), max_length=50)
    description = models.TextField(blank=True)


    def __str__(self):
        return self.name


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='team_pictures/', blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.name
    
class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.question

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()
    received_at = models.DateTimeField(default=timezone.now)
    responded_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class PricingPage(models.Model):
    plan_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.TextField()
    plan_description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.plan_name
    
class PaymentPage(models.Model):
    payment_method = models.CharField(max_length=100)
    description = models.TextField()
    additional_info = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.payment_method
    
class CheckoutPage(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    order_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=100, default='Pending')
    customer_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.product_name

class HelpCenter(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=100, blank=True, null=True)
    related_articles = models.ManyToManyField('self', blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

