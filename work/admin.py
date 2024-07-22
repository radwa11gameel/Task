# admin.py
from django.contrib import admin
from .models import Task, Home, Feature, Service,TeamMember, FAQ, Contact, PricingPage, PaymentPage, CheckoutPage, HelpCenter

admin.site.register(Task)


admin.site.register(Home)


admin.site.register(Feature)


admin.site.register(Service)


admin.site.register(TeamMember)
    

admin.site.register(FAQ)
    

admin.site.register(Contact)


admin.site.register(PricingPage)


admin.site.register(PaymentPage)


admin.site.register(CheckoutPage)


admin.site.register(HelpCenter)
