from django.shortcuts import render,redirect,get_object_or_404
from .forms import Admin_LoginForm
from .models import CarDetails,Booking
from user.models import CancelledBooking
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def admin_navbar(request):
    return render(request,'include/admin_navbar.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('admin_index')  
        else:
            error = "Invalid credentials or not a superuser"
            return render(request, 'adminlogin.html', {'form': Admin_LoginForm(), 'error': error})

    form = Admin_LoginForm()
    return render(request, 'adminlogin.html', {'form': form})

@login_required(login_url='admin_login')
def admin_index(request):
   

    if request.method == 'POST':
        carname = request.POST.get('carname')
        modelyear = request.POST.get('modelyear')
        cartype = request.POST.get('cartype')
        geartype = request.POST.get('geartype')
        fueltype = request.POST.get('fueltype')
        seating = request.POST.get('seating')
        fastag = True if request.POST.get('fastag') == 'on' else False
        price = request.POST.get('price')
        deposit = request.POST.get('deposit')
        

        # # Handle features (multiple checkboxes)
        # selected_features = request.POST.getlist('features')
        # features_str = ",".join(selected_features)

        # Handle uploaded images
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')

        CarDetails.objects.create(
            carname=carname,
            modelyear=modelyear,
            cartype=cartype,
            geartype=geartype,
            fueltype=fueltype,
            seating=seating,
            fastag=fastag,
            price=price,
            deposit=deposit,
            
            # features=features_str,
            image1=image1,
            image2=image2,
            image3=image3
        )

        return redirect('admin_index')
        

    all_cars = CarDetails.objects.all().order_by('-created_at') 
    
    return render(request, 'admin_dashboard.html', {'cars': all_cars})

@login_required(login_url='admin_login')
def delete_car(request,id):
    select_cars=CarDetails.objects.get(id=id)
    select_cars.delete()
    return redirect('admin_index')

@login_required(login_url='admin_login')
def update_car(request, id):
    car1 = get_object_or_404(CarDetails, id=id)

    if request.method == "POST":
        car1.carname = request.POST.get('carname')
        car1.modelyear = request.POST.get('modelyear')
        car1.cartype = request.POST.get('cartype')
        car1.geartype = request.POST.get('geartype')
        car1.fueltype = request.POST.get('fueltype')
        car1.seating = request.POST.get('seating')
        car1.fastag = True if request.POST.get('fastag') == 'on' else False
        car1.price = request.POST.get('price')
        car1.deposit = request.POST.get('deposit')
        

        # features = request.POST.getlist('features')
        # car1.features = ",".join(features)

        if request.FILES.get('image1'):
            car1.image1 = request.FILES['image1']
        if request.FILES.get('image2'):
            car1.image2 = request.FILES['image2']
        if request.FILES.get('image3'):
            car1.image3 = request.FILES['image3']

        car1.save()
        return redirect('admin_index')

    return render(request, 'update.html', {'car': car1})


@login_required(login_url='admin_login')
def view_orders(request):
    bookings = Booking.objects.select_related('CarDetails').all().order_by('-created_at')
    cancelled_booking = CancelledBooking.objects.all().order_by('-created_at') 

    context = {
        'bookings': bookings,
        'cancelled_booking':cancelled_booking
    }

    return render(request, 'view_orders.html', context)

@login_required(login_url='admin_login')
def update_booking_status(request, id):
    if request.method == 'POST':
        booking = get_object_or_404(Booking, id=id)
        new_status = request.POST.get('status')
        booking.status = new_status
        booking.save()

       
        car = booking.CarDetails
        if new_status in ('Confirmed', 'Pending'):
            car.availability = 'Not Available'
        elif new_status in ('Complete','Cancelled'):
            car.availability = 'Available'
        car.save()

        return redirect('view_orders')
    
@login_required(login_url='admin_login')
def cancel_booking(request, id):
    cancel_booking = get_object_or_404(Booking, id=id)

    # Backup data before deleting
    CancelledBooking.objects.create(
        CarDetails=cancel_booking.CarDetails,
        customername=cancel_booking.customername,
        email=cancel_booking.email,
        mobilenumber=cancel_booking.mobilenumber,
        licencenumber=cancel_booking.licencenumber,
        licenceimage=cancel_booking.licenceimage,
        bookingdate=cancel_booking.cancel_bookingdate,
        pickup_datetime=cancel_booking.pickup_datetime,
        drop_datetime=cancel_booking.drop_datetime,
        total_hours=cancel_booking.total_hours,
        total_price=cancel_booking.total_price,
        user_id=cancel_booking.user_id,
    )

    # Delete the original cancel_booking
    cancel_booking.delete()

    return redirect('view_orders')
    
@login_required(login_url='admin_login')
def admin_logout(request):
    logout(request)
    return redirect('admin_login') 

