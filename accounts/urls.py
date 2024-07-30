from django.urls import path
from .views import *
from . import views
from django.contrib.auth import  views as auth_views


app_name = 'accounts'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', user_registration, name='register'),
    path('complete_profile/',complete_profile,name='complete_profile'),
    path('address_details/',address_details,name='address_details'),
    path('employment_details/',employment_details,name='employment_details'),
    path('educational_details/',educational_details.as_view(),name='educational_details'),
    path('about_details/',about_details,name='about_details'),
    path('relation/',relation.as_view(),name='relation'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile_edit/',ProfileUpdateView.as_view(),name ='profile_edit'),
    path('address_edit/',AddressUpdateView.as_view(),name ='address_edit'),
    path('employ_edit/',EmploymentUpdateView.as_view(),name ='employ_edit'),
    path('additional_edit/',AdditionalUpdateView.as_view(),name ='additional_edit'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('delete-account/', delete_account_view, name='delete_account'),
    path('password_reset/', custom_password_reset_request, name='custom_password_reset_request'),
    path('reset/<uidb64>/<token>/', custom_password_reset_confirm, name='custom_password_reset_confirm'),
]