from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import User  # Import your custom User model

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Optionally, customize the admin view for the User model
    model = User
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
