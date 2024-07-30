from django.db import IntegrityError

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from typing import Any

from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .forms import *
from django.views.generic import View,TemplateView,FormView,UpdateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail

# Create your views here.
class LoginView(View):
    def get(self, request):
        context = {'form': LoginForm()}
        return render(request, 'registration/login.html', context)
    
    def post(self, request):
        form = LoginForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                # Check if the user is an admin
                if user.is_superuser:
                    return redirect('app:dashboard')  # Redirect to the admin dashboard
                else:
                    return redirect('app:list_profiles')  # Redirect to the profiles list
            else:
                context['error'] = 'Invalid username or password.'
        
        return render(request, 'registration/login.html', context)
                
        
            


def user_registration(request):
    context = {}

    if request.method == 'GET':
        context['form'] = RegistrationForm()
        return render(request, 'registration/register.html', context)

    elif request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        context['form'] = form

        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password'])
                user.save()
                login(request, user)
                messages.success(request,f'Account created for {user.username}!')
                return redirect('accounts:complete_profile')
            except IntegrityError as e:
                # Handle unique constraint violations (e.g., duplicate username)
                print(f"Error during registration: {e}")
                context['error'] = "There was an error during registration. Please try again."
                return render(request, 'registration/register.html', context)
        else:
            print('No post method')
            return render(request, 'registration/register.html', context)
        



def complete_profile(request):
    if request.method == 'POST':
         
        form = UserProfileForm(request.POST,request.FILES, instance=request.user)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.save()
                messages.success(request,'Your Profile has been updated!')
                return redirect('accounts:address_details')
            except IntegrityError as e:
                # Handle unique constraint violations (e.g., duplicate username)
                print(f"Error during registration: {e}")
                
                return render(request, 'registration/register.html')
            
    else:
        form = UserProfileForm(instance=request.user)  
    return render(request,'registration/complete_profile.html',{'form':form})





def address_details(request):
    
    if request.method == 'POST':
        form = AddressForm(request.POST)
       
        if form.is_valid():
            try:
                address = form.save(commit=False)
                address.user = request.user
                address.save()
                messages.success(request,'Your Address has been updated!')
                return redirect('accounts:employment_details')
            except IntegrityError as e:
                print(f"Error:{e} ")
                return render(request,'registration/register.html')
            
    else:
        form = AddressForm()
    return render(request,'registration/address_details.html',{'form':form})
        




    
def employment_details(request):
    if request.method == 'POST':
        form = EmploymentForm(request.POST,instance=request.user)
        if form.is_valid():
            try:
                employment_details = form.save(commit=False)
                
                employment_details.save()
                messages.success(request,'Your Address has been updated!')
                return redirect('accounts:relation')
            except IntegrityError as e:
                print(f"Error:{e} ")
                return render(request,'registration/register.html')
            
    else:
        form = EmploymentForm(instance=request.user)
    return render(request,'registration/employment_details.html',{'form':form})


def about_details(request):
    if request.method == 'POST':
        form = AboutForm(request.POST,instance=request.user)
        if form.is_valid():
            try:
                about_details = form.save(commit=False)
                
                about_details.save()
                messages.success(request, 'Your details have been updated!')
                return redirect('app:list_profiles')
            except IntegrityError as e:
                messages.error(request, f"Error: {e}")
                return render(request, 'registration/about_details.html', {'form': form})
        else:
            messages.error(request, "There were errors in your form. Please correct them and try again.")
    else:
        form = AboutForm(instance=request.user)
    
    return render(request, 'registration/about_details.html', {'form': form})




class educational_details(TemplateView):
    template_name = 'registration/educational_details.html'
    


    
class relation(TemplateView):
    template_name = 'registration/relation.html'


class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('/')    
    
    
        
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'user/view.html'
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        user=self.request.user
        context['data'] = self.request.user
        context['address'] = Address.objects.get(user=user)
        context['family'] = Family.objects.get(user = user)
        context['partner'] =Partner.objects.get(user = user)
        return context
    
class ProfileUpdateView(LoginRequiredMixin,UpdateView):
    model = User
    form_class = ProfileUpdateForm
    template_name = 'registration/profile_update.html'
    success_url = reverse_lazy('accounts:profile')
    
    def get_object(self):
        return self.request.user
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
    
class AdditionalUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'registration/additional_update.html'
    success_url = reverse_lazy('accounts:profile')
    
    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

    
class AddressUpdateView(LoginRequiredMixin, UpdateView):
    model = Address
    form_class = AddressForm
    template_name = 'registration/address_update.html'
    success_url = reverse_lazy('accounts:profile')
    
    def get_object(self):
        return Address.objects.get(user=self.request.user)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class EmploymentUpdateView(LoginRequiredMixin,UpdateView):
    model = User
    form_class = EmploymentForm
    template_name = 'registration/employ_update.html'
    success_url = reverse_lazy('accounts:profile')
       
    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

class ChangePasswordView(PasswordChangeView):
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('accounts:profile')
    
    def form_valid(self,form):
        self.request.user.set_password(form.cleaned_data['new_password1'])
        self.request.user.save()
        messages.success(self.request, 'Your password was successfully updated!')
        return HttpResponseRedirect(self.get_success_url())      
    
@login_required
def delete_account_view(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        messages.success(request, 'Your account has been deleted successfully.')
        return redirect('accounts:register')  # Adjust to your desired redirect URL after account deletion
    
    return render(request, 'registration/delete_account.html')
    
def custom_password_reset_request(request):
    if request.method == "POST":
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.get(email=email)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            password_reset_url = request.build_absolute_uri(
                reverse('accounts:custom_password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
            )

            # Send the custom password reset email
            subject = "Password Reset Requested"
            message = render_to_string('registration/custom_password_reset_email.html', {
                'user': user,
                'password_reset_url': password_reset_url,
            })
            send_mail(subject, message, 'admin@yourdomain.com', [user.email])

            messages.success(request, 'A password reset link has been sent to your email.')
            return redirect('accounts:login')
    else:
        form = CustomPasswordResetForm()
    return render(request, 'registration/custom_password_reset_form.html', {'form': form})

def custom_password_reset_confirm(request, uidb64, token):
    user = None
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == "POST":
            new_password = request.POST.get('new_password')
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Your password has been reset successfully.')
            return redirect('accounts:login')
        return render(request, 'registration/custom_password_reset_confirm.html', {'user': user})
    else:
        messages.error(request, 'The password reset link is invalid.')
        return redirect('accounts:custom_password_reset_request')