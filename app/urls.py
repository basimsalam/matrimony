from django.contrib import admin
from django.urls import path,include,reverse
from .views import *

from . import views



app_name = 'app'
urlpatterns = [
    path('index/',views.index,name='index'),
    
    path('dashboard/',views.dashboard,name='dashboard'),
    path('usermanage/',views.usermanage,name='usermanage'),
    path('billing/',views.billing,name='billing'),
    path('adminprofile/',views.adminprofile,name='adminprofile'),
    path('contentmanage/',views.contentmanage,name='contentmanage'),
   
    # path('userlogin/',views.userlogin,name='userlogin'),
   
   
    path('support/',views.support,name='support'),
    
    
   
   
   
    
    path('family_details/',family_details,name='family_details'),
    path('partner/',partner,name='partner'),
   
    
    path('', HomeView.as_view(), name='home'),
    path('pview/', pview.as_view(), name='pview'),
    path('notification/',notification.as_view(),name='notification'),
    path('list_profiles/', ProfileListView.as_view(), name='list_profiles'),
    path('detailed_profile/<int:id>/', detailed_profile, name='detailed_profile'),
    path('change_profile/', change_profile_picture, name='change_profile'),
    path('upload_files/', upload_files, name='upload_files'),
    path('send_friend_request/<int:user_id>/', views.send_friend_request, name='send_friend_request'),
    path('accept_friend_request/<int:request_id>/', views.accept_friend_request, name='accept_friend_request'),
    path('delete_friend_request/<int:request_id>/', views.delete_friend_request, name='delete_friend_request'),
    path('unfriend/<int:user_id>/', unfriend, name='unfriend'),
    path('received_requests/', views.received_requests, name='received_requests'),
    path('shortlist/<int:user_id>/', shortlist_profile, name='shortlist_profile'),
    path('favorites/', favorite_profiles, name='favorite_profiles'),
    path('remove_from_favorites/<int:profile_id>/', remove_from_favorites, name='remove_from_favorites'),
    
    path('chat/<int:id>/', views.messaging_page, name='messaging_page'),
    path('send_message/', views.send_message, name='send_message'),
    path('get_messages/<int:id>/', views.get_messages, name='get_messages'),
    path('not_premium/',not_premium,name='not_premium'),
    
    
    
    
    
    
    
    
   
]