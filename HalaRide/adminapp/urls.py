from django.urls import path
from . import views

urlpatterns = [
    path('adminnavbar/', views.admin_navbar, name='admin_navbar'), 
    path('adminlogin/', views.admin_login, name='admin_login'),
    path('adminlogout/', views.admin_logout, name='admin_logout'), 
    path('admindashboard/', views.admin_index, name='admin_index'), 
    path('orders/', views.view_orders, name='view_orders'),
    path('delete_car/<int:id>/', views.delete_car, name='delete'),
    path('update_car/<int:id>/', views.update_car, name='update'),
    path('update_booking_status/<int:id>/', views.update_booking_status, name='update_status'),
    
]