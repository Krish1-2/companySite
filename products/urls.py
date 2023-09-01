from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RateView, Register, Login

urlpatterns = [
    path('', RateView.as_view(), name='rate'),
    path('api/user/login/', Login.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('api/user/register/', Register.as_view(), name='register'),  # Updated URL path
]
