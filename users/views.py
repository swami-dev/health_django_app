from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm, LoginForm
from django.contrib.auth import get_user_model
User = get_user_model()

# Register view
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # After registration, redirect to login page
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

# Login view
# Login view
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect already logged-in users

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)  # Pass `request` explicitly
        if form.is_valid():
            # Authenticate and login user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')  # Redirect after successful login
            else:
                form.add_error(None, "Invalid username or password")  # General error
    else:
        form = LoginForm()  # GET request

    return render(request, 'users/login.html', {'form': form})


# Home view
def home(request):
    return render(request, 'users/home.html')

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout
