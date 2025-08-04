# Car Rental Management System

A full-stack web application built with **Python (Django)** for backend and **HTML/CSS/Bootstrap** for frontend.  
It digitizes and automates the car rental process—allowing customers to browse, book, and enabling administrators to manage cars and bookings through a secure admin panel.

## Features

### Customer
Sign up and securely log in.
Browse available cars with details.
Select preferred rental dates and book a car.

### Admin
Secure admin login.
Add, edit, or remove car listings.
View all user bookings.
Check booked cars and their reserved dates.
Prevent double-booking via date conflict checks.

### Core Logic
Booking Confirmation Logic:
When a customer books a car, the booking details are displayed in the admin panel. The administrator can update the booking status to Confirmed or Pending. For these statuses, the car will be marked as Not Available (displayed in red) on the customer page. If the booking status is changed to Cancelled or Completed, the car will be marked as Available (displayed in green) on the customer page.

## Tech Stack
Backend: Python, Django
Frontend: HTML, CSS, Bootstrap
Database: Relational (e.g., SQLite for development)
Code Editor: Visual Studio Code


