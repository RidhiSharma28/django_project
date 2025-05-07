from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Homepage View
def homepage_view(request):
    return render(request, "firstapptemplates/HomePage.html")

# Dashboard View
@login_required
def dashboard_view(request):
    return render(request, 'firstapptemplates/Dashboard.html', {'user': request.user})

# Login View
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Check if the user exists with the given email and authenticate
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful! Welcome back.")
            return redirect('dashboard')  # Redirect to dashboard after successful login
        else:
            messages.error(request, "Invalid email or password. Please try again.")
            return redirect('login')  # Redirect back to login if credentials are incorrect

    return render(request, 'firstapptemplates/LoginPage.html')

# Signup View
def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Ensure the email is unique (case-insensitive)
        if User.objects.filter(email=email).exists():
            messages.warning(request, "User with this email already exists. Please login.")
            return redirect('login')

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Account created successfully. Please log in.")
        return redirect('login')

    return render(request, 'firstapptemplates/SignupPage.html')

# Logout View
@login_required
def logout_view(request):
    logout(request)  # Use Django's logout function
    return redirect('home')  # Redirect to home page after logout

# Profile View
@login_required
def profile_view(request):
    return render(request, "firstapptemplates/MyProfile.html", {"user": request.user})
