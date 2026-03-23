from django.contrib import admin
from .models import Salesperson, Customer, Car, SalesInvoice, Mechanic, ServiceTicket, Service, Parts, PartsUsed, ServiceMechanic

# This loop registers every model at once
models = [Salesperson, Customer, Car, SalesInvoice, Mechanic, ServiceTicket, Service, Parts, PartsUsed, ServiceMechanic]
for model in models:
    admin.site.register(model)