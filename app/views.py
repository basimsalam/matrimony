import json
import time
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.forms import AboutForm, FamilyForm,PartnerForm, ProfilePictureForm, ShortlistForm
from app.models import Family,Partner, Shortlist
from accounts.models import *
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from payment.models import UserSubscription

# Create your views here.


def index(request):
    return render(request,'index.html')


@login_required()
def dashboard(request):
    total_users = User.objects.count()
    
    # Calculate number of premium users (assuming you have a boolean field 'is_premium')
    premium_users = UserSubscription.objects.filter(active=True).count()
    
    # Calculate number of male users (assuming you have a gender field)
    male_users = User.objects.filter(gender='Male').count()
    
    # Calculate number of female users
    female_users = User.objects.filter(gender='Female').count()

    context = {
        'total_users': total_users,
        'premium_users': premium_users,
        'male_users': male_users,
        'female_users': female_users,
    }
    return render(request,'dashindex.html',context)


@login_required()
def usermanage(request):
    return render(request,'userm.html')


@login_required()
def billing(request):
    return render(request,'billing.html')


@login_required()
def adminprofile(request):
    return render(request,'adminprofile.html')


@login_required()
def contentmanage(request):
    return render(request,'contentmanage.html')

@login_required()
def support(request):
    return render(request,'support.html')


def usernav(request):
    return render(request,'user/usernav.html')



class HomeView(LoginRequiredMixin,TemplateView):
    template_name = 'user/home.html'
    
class notification(LoginRequiredMixin,TemplateView):
    template_name = 'user/notification.html'

def family_details(request):
    try:
        family = Family.objects.get(user = request.user)
        
    except Family.DoesNotExist:
        family = None
        
    if request.method =='POST':
        form = FamilyForm(request.POST)
        if form.is_valid:
            family=form.save(commit=False)
            family.user = request.user
            family.save()
            return redirect('app:partner')
    else:
        form = FamilyForm()
            
    return render(request,'user/family_details.html',{'form':form})

def partner(request):
    """
    Handles the creation and updating of the Partner model for the logged-in user.
    """
    partner, created = Partner.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = PartnerForm(request.POST, instance=partner)
        if form.is_valid():
            partner = form.save(commit=False)
            partner.user = request.user
            partner.save()
            messages.success(request, 'Partner profile saved successfully.')
            return redirect('accounts:about_details')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PartnerForm(instance=partner)

    return render(request, 'user/partner.html', {'form': form})




class pview(TemplateView):
    template_name = 'user/view.html'
    

class ProfileListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'user/profile_grid.html'
    context_object_name = 'profiles'
    paginate_by = 12

    def get_queryset(self):
        user = self.request.user
        
        if user.interest == 'Male':
            queryset = User.objects.filter(gender='Male')
        elif user.interest == 'Female':
            queryset = User.objects.filter(gender='Female')
        else:
            queryset = User.objects.filter(gender__in=['Male', 'Female'])
        preference = get_object_or_404(Partner,user=self.request.user)
        
        
        queryset = queryset.exclude(id=user.id).exclude(is_staff = True)
        queryset = queryset.select_related('family', 'partner').prefetch_related('address').all()
        
        
        return queryset




def detailed_profile(request,id):
   
    user_details = User.objects.get(id=id)
    similar_profiles = User.objects.filter(
        hobbies = user_details.hobbies
    ).exclude(
        id=user_details.id
    )[:3]
    is_friend = request.user in user_details.friend.all()

    # Check if the request is sent
    request_sent = FriendRequest.objects.filter(from_user=request.user, to_user=user_details).exists()
    
    context = {
        
        'user_details': user_details,
        'similar_profiles': similar_profiles,
        'is_friend': is_friend,
        'request_sent': request_sent,
       
        
    }
    return render(request,'user/desc_profile.html',context)


def change_profile_picture(request):
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile picture updated successfully.')
            return redirect('accounts:profile')
    else:
        form = ProfilePictureForm(instance=request.user)

    return render(request, 'user/view.html', {'form': form})

def upload_files(request):
    if request.method == 'POST' and request.FILES:
        images = request.FILES.getlist('images')
        reels = request.FILES.getlist('reels')
        
        for image in images:
            Image.objects.create(user=request.user, image=image)
        
        for reel in reels:
            Reel.objects.create(user=request.user,reel=reel)
        
        return redirect('accounts:profile')
    
    return render(request, 'registration/upload.html')


def send_friend_request(request, user_id):
    to_user = User.objects.get( pk=user_id)
    from_user = request.user

    existing_request = FriendRequest.objects.filter(from_user=from_user, to_user=to_user).first()

    if existing_request:
        # If there's an existing request, delete it to allow sending a new one
        existing_request.delete()

    if request.method == 'POST':
        FriendRequest.objects.create(from_user=from_user, to_user=to_user)
        return redirect('app:detailed_profile', id=user_id)

    return redirect('app:detailed_profile', id=user_id)

def accept_friend_request(request, request_id):
    friend_request = get_object_or_404(FriendRequest, id=request_id)
    if request.method == 'POST' and friend_request.to_user == request.user:
        friend_request.status = 'accepted'
        friend_request.save()
        sender = friend_request.from_user
        receiver = friend_request.to_user
        
        sender.friend.add(receiver)
        receiver.friend.add(sender)
        
        # Optionally, you can add a success message
        messages.success(request, f'You are now friends with {sender.username}')
        
        # Add each other to friends list, if necessary
        return redirect('app:received_requests')
    return redirect('app:received_requests')

def delete_friend_request(request, request_id):
    friend_request = get_object_or_404(FriendRequest, id=request_id)
    if request.method == 'POST' and (friend_request.to_user == request.user or friend_request.from_user == request.user):
        friend_request.delete()
        return redirect('app:received_requests')
    return redirect('app:received_requests')

def received_requests(request):
    received_requests = FriendRequest.objects.filter(to_user=request.user, status='pending')
    context ={
        'received_requests': received_requests,
    }
    return render(request, 'user/friend_req.html', context)

def unfriend(request, user_id):
    if request.method == 'POST':
        current_user = request.user
        user_to_unfriend = get_object_or_404(User, pk=user_id)
        
        try:
            
            
            # Perform the unfriending action
            current_user.unfriend(user_to_unfriend)
            
            messages.success(request, f'You have unfriended {user_to_unfriend.username}.')
        except User.DoesNotExist:
            messages.error(request, 'UserProfile not found.')
        
        return redirect('app:detailed_profile',id = user_id)  # Redirect to profile or wherever appropriate
    else:
        return redirect('app:detailed_profile',id = user_id)  # Handle GET requests appropriately

def shortlist_profile(request, user_id):
    shortlisted_user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        shortlist, created = Shortlist.objects.get_or_create(user=request.user, shortlisted_user=shortlisted_user)
        if created:
            messages.success(request, f'You have successfully shortlisted {shortlisted_user.username}.')
        else:
            messages.info(request, f'You have already shortlisted {shortlisted_user.username}.')
        return redirect('app:detailed_profile', id=user_id)


def favorite_profiles(request):
    favorites = Shortlist.objects.filter(user=request.user).select_related('shortlisted_user')
    return render(request, 'user/favorites.html', {'favorites': favorites})
    
def remove_from_favorites(request, profile_id):
    profile = get_object_or_404(User, id=profile_id)
    favorite = Shortlist.objects.filter(user=request.user, shortlisted_user=profile)
    if favorite.exists():
        favorite.delete()
    return redirect('app:favorite_profiles')

#+++++++++++++++++++++++++web chat=======================


@login_required
def messaging_page(request, id=None):
    user_details = User.objects.get(id=id)
    try:
        if not request.user.usersubscription.active:
            return redirect('app:not_premium')  # Redirect to the subscription plans page
    except UserSubscription.DoesNotExist:
        return redirect('app:not_premium') 
    users = User.objects.exclude(id=request.user.id)
    receiver = get_object_or_404(User, id=id) if id else None
    is_friend = request.user in user_details.friend.all()
    
    
    if request.user.gender == 'Male':
        users = users.filter(gender='Female')
    elif request.user.gender == 'Female':
        users = users.filter(gender='Male')
    return render(request, 'user/chat.html', {'users': users, 'user_id': id,'receiver': receiver,'is_friend':is_friend})

@csrf_exempt
@login_required
def send_message(request):
    if not request.user.usersubscription.active:
        return JsonResponse({'status': 'Failed', 'error': 'Not a premium member'}, status=403)
    if request.method == 'POST':
        data = json.loads(request.body)
        receiver_id = data.get('receiver_id')
        content = data.get('content')
        receiver = get_object_or_404(User, id=receiver_id)

        message = Message.objects.create(
            sender=request.user,
            receiver=receiver,
            content=content
        )

        return JsonResponse({'status': 'Message sent', 'message_id': message.id})
    return JsonResponse({'status': 'Failed'}, status=400)

@login_required
def get_messages(request, id):
    if not request.user.usersubscription.active:
        return JsonResponse({'status': 'Failed', 'error': 'Not a premium member'}, status=403)
    user = request.user
    receiver = get_object_or_404(User, id=id)
    
    messages = Message.objects.filter(
        (Q(sender=user) & Q(receiver=receiver)) |
        (Q(sender=receiver) & Q(receiver=user))
    ).order_by('timestamp')
    unread_messages = messages.filter(receiver=user, status='delivered')
    unread_messages.update(status='read')
    message_list = [{
        'sender': message.sender.username,
        'receiver': message.receiver.username,
        'content': message.content,
        'timestamp': message.timestamp.strftime('%H:%M'),
        'status': message.status,
    } for message in messages]

    return JsonResponse({'messages': message_list})

#+++++++++++++++++++++++++web chat=======================

def not_premium(request):
    return render(request, 'user/not_premium.html')
