from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from .views import RateView,Register,Login,getReview,Logout
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('',RateView.as_view(),name='rate'),
    path('api/user/login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('api/user/register/', Register.as_view(), name='register'),
     path('review', getReview.as_view(), name='review'),
      path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
