from django.db import models
from datetime import date
from user.models import Signup

class CarDetails(models.Model):
    image1 = models.ImageField(upload_to='car_images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='car_images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='car_images/', null=True, blank=True)

    carname = models.CharField(max_length=100,default='Car name')
    modelyear = models.IntegerField(default=2000)

    cartype = models.CharField(max_length=20,default='suv')
    geartype = models.CharField(max_length=10,default='Automatic')
    fueltype = models.CharField(max_length=10,default='Petrol')
    seating = models.CharField(max_length=10,default=5)
    fastag = models.BooleanField(default=False)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    deposit = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.carname
    
class Booking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
        ('Completed', 'Completed'),
    ]
    
    user = models.ForeignKey(Signup, on_delete=models.CASCADE, null=True)

    # 🔗 Connect to CarDetails, but allow deletion
    CarDetails = models.ForeignKey('CarDetails', on_delete=models.SET_NULL, null=True, blank=True)

    # 🔽 Booking info
    customername = models.CharField(max_length=100, default='customer name')
    email = models.EmailField(default='example@gmail.com')
    mobilenumber = models.BigIntegerField(default=9999999999)
    licencenumber = models.CharField(max_length=10, default='NA12345678')
    licenceimage = models.ImageField(upload_to='Licence/', null=True, blank=True)
    address = models.CharField(max_length=225, default='Tamil Nadu')
    bookingdate = models.DateField(default=date.today)

    pickup_datetime = models.DateTimeField(null=True, blank=True)
    drop_datetime = models.DateTimeField(null=True, blank=True)
    total_hours = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    
    car_image = models.ImageField(upload_to='car_snapshots/', null=True, blank=True)
    carname = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    deposit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customername