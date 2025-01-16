from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

# Define urlpatterns first
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),  # Redirect target after login
    path('logout/', views.logout_view, name='logout'),  # Logout functionality
]

# Add media URL configuration for development (only if DEBUG is True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
