from django.urls import path
from .views import register, CustomLoginView, CustomLogoutView, home,profile, landing

urlpatterns = [
    path('landing/', landing, name='landing'),
    path('register/', register, name='register'),
    path('home/', home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile')
]
