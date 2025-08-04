
from django.urls import path
from . import views

urlpatterns = [
    path('usernavber/', views.user_navbar, name='user_navbar'), 
    path('footer/', views.footer, name='footer'),
    path('', views.index, name='index'), 
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'), 
    path('logout/', views.log_out, name='logout'), 
    path('carlist/', views.carlist, name='carlist'),  
    path('cardetails/<int:id>/', views.cardetails, name='cardetails'),  
    path('booking/<int:id>/', views.booking, name='booking'),
    path('mybookings/', views.mybookings, name='mybookings'), 
    path('cancelbooking/<int:id>/', views.cancel_booking, name='cancelbooking'),
    path('sedan/', views.sedan_cars, name='sedan_cars'),
    path('hatchback/',views.hatchback, name='hatchback'),
    path('suv/',views.suv, name='suv'),
    path('mpv/',views.mpv, name='mpv'),


    
    
]
