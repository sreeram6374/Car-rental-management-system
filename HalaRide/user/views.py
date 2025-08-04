from django.shortcuts import render,redirect,get_object_or_404
from .forms import SignupForm,LoginForm,CarSearchForm
from .models import Signup,CancelledBooking
from adminapp.models import CarDetails,Booking 

from datetime import datetime
from decimal import Decimal 
from django.contrib import messages 


def user_navbar(request):
    return render(request,'include/user_navbar.html')



def footer(request):
    return render(request,'include/footer.html')



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
        

    return render(request, 'signup.html', {'signup_form': form}) 

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            
            user = Signup.objects.filter(email=email, password=password).first()

            if user:
                request.session['user_id'] = user.id
                request.session['email'] = user.email
                return redirect('index')


    else:
        form = LoginForm()

    return render(request, 'login.html', {'login_form': form})

def log_out(request):
    request.session.flush()
    return redirect('login')


def index(request):
    if request.method == 'POST':
        SearchForm = CarSearchForm(request.POST)
        if SearchForm.is_valid():
            # cleaned data
            car_type = SearchForm.cleaned_data.get('car_type')
            seats = SearchForm.cleaned_data.get('seats')
            transmission = SearchForm.cleaned_data.get('transmission')

            # Use model field names in GET parameters
            return redirect(f"/carlist/?cartype={car_type}&seating={seats}&geartype={transmission}")
    else:
        SearchForm = CarSearchForm()

    return render(request, 'index.html', {'SearchForm': SearchForm})


def carlist(request):
    search_query = request.GET.get('search', '')
    cartype = request.GET.get('cartype')
    seating = request.GET.get('seating')
    geartype = request.GET.get('geartype')

    cars = CarDetails.objects.all().order_by('-created_at')

    # Filter by car name
    if search_query:
        cars = cars.filter(carname__icontains=search_query)

    if cartype:
        cars = cars.filter(cartype=cartype)

    if seating:
        cars = cars.filter(seating=seating)

    if geartype:
        cars = cars.filter(geartype=geartype)

    return render(request, 'carlist.html', {'cars': cars})


def cardetails(request,id):
    car = get_object_or_404(CarDetails, id=id)

    return render(request, 'cardetails.html', {'car': car})


def booking(request, id):
    car = get_object_or_404(CarDetails, id=id)

    if request.method == 'POST':
        if 'user_id' not in request.session:
            return redirect('login')

        user = Signup.objects.get(id=request.session['user_id'])  

        # Get data from form
        customername = request.POST.get('customername')
        email = request.POST.get('email')
        mobilenumber = request.POST.get('mobilenumber')
        licencenumber = request.POST.get('licencenumber')
        address = request.POST.get('address')
        licenceimage = request.FILES.get('licenceimage')
        pickup_datetime = request.POST.get('pickup_datetime')
        drop_datetime = request.POST.get('drop_datetime')

        # Convert string to datetime
        pickup_dt = datetime.fromisoformat(pickup_datetime)
        drop_dt = datetime.fromisoformat(drop_datetime)

        if drop_dt <= pickup_dt:
            messages.error(request, "Drop date & time must be after pickup date & time.")
            return render(request, 'booking.html', {'car': car})

        total_seconds = Decimal((drop_dt - pickup_dt).total_seconds())
        total_hours = total_seconds / Decimal('3600')
        total = total_hours * car.price 
        total_price = total + car.deposit 
        # Save booking
        Booking.objects.create(
            user=user,
            CarDetails=car,
            customername=customername,
            email=email,
            mobilenumber=int(mobilenumber),
            licencenumber=licencenumber,
            licenceimage=licenceimage,
            address=address,
            pickup_datetime=pickup_dt,
            drop_datetime=drop_dt,
            car_image=car.image1,
            carname=car.carname,
            price=car.price,
            deposit=car.deposit,
            total_hours=total_hours,
            total_price=total_price 
        )

        return redirect('mybookings')

    return render(request, 'booking.html', {'car': car})

def mybookings(request):
    if 'user_id' not in request.session:
        return redirect('login')

    user_id = request.session['user_id']

    my_book_data = Booking.objects.filter(user_id=user_id)
    cancelled_data = CancelledBooking.objects.filter(user_id=user_id)  

    return render(request, 'mybookings.html', {
        'my_book_data': my_book_data,
        'cancelled_data': cancelled_data,
    })


def cancel_booking(request, id):
    booking = get_object_or_404(Booking, id=id)

    CancelledBooking.objects.create(
        user=booking.user,
        # CarDetails=booking.CarDetails,
        
        # Snapshot values
        car_image1=booking.CarDetails.image1 if booking.CarDetails else booking.car_image1,
        carname=booking.CarDetails.carname if booking.CarDetails else booking.carname,
        price=booking.CarDetails.price if booking.CarDetails else booking.price,
        deposit=booking.CarDetails.deposit if booking.CarDetails else booking.deposit,

        customername=booking.customername,
        email=booking.email,
        mobilenumber=booking.mobilenumber,
        licencenumber=booking.licencenumber,
        licenceimage=booking.licenceimage,
        address=booking.address,
        bookingdate=booking.bookingdate,
        pickup_datetime=booking.pickup_datetime,
        drop_datetime=booking.drop_datetime,
        total_hours=booking.total_hours,
        total_price=booking.total_price,
        status=booking.status,
    )

    booking.delete()

    return redirect('mybookings')


def sedan_cars(request):
    sedan_cars = CarDetails.objects.filter(cartype='Sedan')
    return render(request, 'carlist.html', {'cars': sedan_cars})


def hatchback(request):
    hatchback_cars = CarDetails.objects.filter(cartype='Hatchback')
    return render(request, 'carlist.html', {'cars': hatchback_cars})

def suv(request):
    suv_car = CarDetails.objects.filter(cartype='SUV')
    return render(request, 'carlist.html', {'cars': suv_car})

def mpv(request):
    mpv_car = CarDetails.objects.filter(cartype='MPV')
    return render(request, 'carlist.html', {'cars': mpv_car})