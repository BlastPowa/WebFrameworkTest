from django.db import models

class Salesperson(models.Model):
    sales_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)

    class Meta:
        db_table = 'tbl_salespeople'

class Customer(models.Model):
    cust_id = models.AutoField(primary_key=True)
    given_name = models.CharField(max_length=50)
    family_name = models.CharField(max_length=50)
    contact_phone = models.CharField(max_length=20)
    street_address = models.CharField(max_length=100)
    loc_city = models.CharField(max_length=50)
    loc_region = models.CharField(max_length=50)
    loc_country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)

class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    vin_number = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    paint_color = models.CharField(max_length=20)
    mfg_year = models.IntegerField()
    for_sale = models.BooleanField(default=True)

class SalesInvoice(models.Model):
    inv_id = models.AutoField(primary_key=True)
    inv_number = models.CharField(max_length=50)
    sale_date = models.DateField()
    vehicle = models.ForeignKey(Car, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    seller = models.ForeignKey(Salesperson, on_delete=models.CASCADE)

class Mechanic(models.Model):
    mech_id = models.AutoField(primary_key=True)
    mech_fname = models.CharField(max_length=50)
    mech_lname = models.CharField(max_length=50)

class ServiceTicket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    ticket_ref = models.CharField(max_length=50)
    received_on = models.DateField()
    returned_on = models.DateField(null=True, blank=True)
    staff_notes = models.TextField()
    vehicle = models.ForeignKey(Car, on_delete=models.CASCADE)
    client = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Service(models.Model):
    svc_id = models.AutoField(primary_key=True)
    svc_name = models.CharField(max_length=100)
    rate_per_hour = models.DecimalField(max_digits=10, decimal_places=2)

class Parts(models.Model):
    part_id = models.AutoField(primary_key=True)
    sku_number = models.CharField(max_length=50)
    part_desc = models.CharField(max_length=255)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)

class PartsUsed(models.Model):
    usage_id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Parts, on_delete=models.CASCADE)
    ticket = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)
    qty_used = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

class ServiceMechanic(models.Model):
    assignment_id = models.AutoField(primary_key=True)
    ticket = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)
    action = models.ForeignKey(Service, on_delete=models.CASCADE)
    worker = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    labor_hours = models.DecimalField(max_digits=5, decimal_places=2)
    work_comment = models.TextField()
    billing_rate = models.DecimalField(max_digits=10, decimal_places=2)