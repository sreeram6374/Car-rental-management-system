from django.db import models
from datetime import date


class Signup(models.Model):
    email=models.EmailField(unique=True)
    password = models.CharField(max_length=128)

class CancelledBooking(models.Model):
    user = models.ForeignKey(Signup, on_delete=models.CASCADE, null=True) 
    CarDetails = models.ForeignKey('adminapp.CarDetails', on_delete=models.SET_NULL, null=True, blank=True)

    # Snapshot fields
    car_image1 = models.ImageField(upload_to='car_snapshots/', null=True, blank=True)
    carname = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    deposit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    customername = models.CharField(max_length=100, default='customer name')
    email = models.EmailField(default='example@gmail.com')
    mobilenumber = models.BigIntegerField(default=9999999999)
    licencenumber = models.CharField(max_length=10, default='NA12345678')
    licenceimage = models.ImageField(upload_to='Licence/', null=True, blank=True)
    pickup_datetime = models.DateTimeField()
    drop_datetime = models.DateTimeField()
    address = models.CharField(max_length=225, default='Tamil Nadu')
    bookingdate = models.DateField(default=date.today)

    pickup_datetime = models.DateTimeField(null=True, blank=True)
    drop_datetime = models.DateTimeField(null=True, blank=True)
    total_hours = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customername

    


