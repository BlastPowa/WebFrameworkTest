from django.db import models

class Salesperson(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state_province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)

class Car(models.Model):
    serial_number = models.CharField(max_length=50)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    year = models.IntegerField()
    is_new = models.BooleanField(default=True)

class SalesInvoice(models.Model):
    invoice_number = models.CharField(max_length=50)
    date = models.DateField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salesperson = models.ForeignKey(Salesperson, on_delete=models.CASCADE)

class Mechanic(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class ServiceTicket(models.Model):
    service_ticket_number = models.CharField(max_length=50)
    date_received = models.DateField()
    date_returned = models.DateField(null=True, blank=True)
    comments = models.TextField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Service(models.Model):
    service_name = models.CharField(max_length=100)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)

class Parts(models.Model):
    part_number = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)