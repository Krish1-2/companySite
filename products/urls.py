from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from .views import RateView,Register,Login,getReview

urlpatterns = [
    path('',RateView.as_view(),name='rate'),
    path('api/user/login/', Login.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('api/user/register/', Register.as_view(), name='register'),
     path('review', getReview.as_view(), name='review'),
]
