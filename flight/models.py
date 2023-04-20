from django.db import models
from django.contrib.auth.models import AbstractUser

from datetime import datetime

# Create your models here.

class User(AbstractUser):
    def __str__(self):
        return f"{self.id}: {self.first_name} {self.last_name}"

class Place(models.Model):
    city = models.CharField(max_length=64)
    airport = models.CharField(max_length=64)
    code = models.CharField(max_length=3)
    country = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city}, {self.country} ({self.code})"

class adven_place(models.Model):
    city = models.CharField(max_length=64)
    code = models.CharField(max_length=3)
    country = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city}, {self.country} ({self.code})"

class Week(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.name} ({self.number})"

class adven_booking(models.Model):
    origin = models.ForeignKey(adven_place, on_delete=models.CASCADE, related_name="depart", default="1")
    destination = models.ForeignKey(adven_place, on_delete=models.CASCADE, related_name="dest")
    check_in_timing = models.TimeField(auto_now=False, auto_now_add=False)
    check_in_day = models.ManyToManyField(Week, related_name="checkin_day")
    duration = models.DurationField(null=True)
    check_out_time = models.TimeField(auto_now=False, auto_now_add=False)
    resort = models.CharField(max_length=64)
    adven = models.CharField(max_length=64)
    regular_fare = models.FloatField(null=True)
    premium_fare = models.FloatField(null=True)

    def __str__(self):
        return f"{self.id}: {self.origin} for {self.adven}"

GENDER = (
    ('male','MALE'),    #(actual_value, human_readable_value)
    ('female','FEMALE')
)

class Passenger(models.Model):
    first_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER, blank=True)
    #passenger = models.ForeignKey(User, on_delete=models.CASCADE, related_name="flights")
    #flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="passengers")

    def __str__(self):
        return f"Passenger: {self.first_name} {self.last_name}, {self.gender}"

SERVICE_CLASS = (
    ('regular', 'Regular'),
    ('premium', 'Premium')
)

ADVEN_BOOKING_STATUS =(
    ('PENDING', 'Pending'),
    ('CONFIRMED', 'Confirmed'),
    ('CANCELLED', 'Cancelled')
)

CURRENCY =(
    ('USD', 'Usd'),
    ('CAD', 'Cad')
)

class adven_Ticket_Model(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_bookings", blank=True, null=True)
    ref_no = models.CharField(max_length=6, unique=True)
    passengers = models.ManyToManyField(Passenger, related_name="user_flight_tickets")
    adven = models.ForeignKey(adven_booking, on_delete=models.CASCADE, related_name="user_adven_tickets", blank=True, null=True)
    adven_ddate = models.DateField(blank=True, null=True)
    adve_adate = models.DateField(blank=True, null=True)
    adven_fare = models.FloatField(blank=True,null=True)
    other_charges = models.FloatField(blank=True,null=True)
    total_fare = models.FloatField(blank=True, null=True)
    currency = models.CharField(max_length=20, choices=CURRENCY)
    service_class = models.CharField(max_length=20, choices=SERVICE_CLASS)
    booking_date = models.DateTimeField(default=datetime.now)
    mobile = models.CharField(max_length=20,blank=True)
    email = models.EmailField(max_length=45, blank=True)
    status = models.CharField(max_length=45, choices=ADVEN_BOOKING_STATUS)

    def __str__(self):
        return self.ref_no

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return self.name