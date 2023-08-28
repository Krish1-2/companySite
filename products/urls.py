from django.urls import path,include
from . import views
from .views import RateView

urlpatterns = [
    # path('',UserLoginView.as_view(),name='auth'),
    path('',RateView.as_view(),name='rate')
]
