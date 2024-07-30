from django.urls import path
from .views import *
from . import views
from django.contrib.auth import  views as auth_views


app_name = 'accounts'
urlpatterns = [
    path('pay/<int:plan_id>/', PaymentView.as_view(), name='payment'),
    path('payment_success/', payment_success, name='payment_success'),
    path('payment_error/<int:plan_id>/', payment_error, name='payment_error'),
    path('plans/', plan_list, name='plan_list'),
]