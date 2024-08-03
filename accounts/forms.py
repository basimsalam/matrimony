
from django import forms
from django.forms import DateInput, Form, ModelForm, CharField, NumberInput, Select, TextInput, PasswordInput, EmailField, EmailInput,FileInput,BooleanField
from .models import  User,Address,FriendRequest,Message
from app.models import Family,Partner, Shortlist

class LoginForm(Form):
    """
    Form for user login.

    Attributes:
        email (EmailField): Field for user email.
        password (CharField): Field for user password.

    """
    username = CharField(
        min_length=4,
        max_length=50,
        label='Username',
        required=True,
    
        widget=TextInput({
            'class': 'form-control',
            
        })
    )

    # Field for user password.
    password = CharField(
        min_length=4,
        max_length=25,
        label='Password',
        required=True,
        widget=PasswordInput({
            'class': 'form-control',
           
        })
    )


class RegistrationForm(ModelForm):
    """
    Form for user registration.

    Attributes:
        confirm_password (CharField): Field for confirming password.

    """
    confirm_password = CharField(
        min_length=8,
        max_length=50,
        label='Confirm Password',
        required=True,
        widget=PasswordInput({
            'class': 'form-control'
        })
    )
    
    class Meta:
        """
        Meta class for RegistrationForm.

        Attributes:
            model (User): The model for the form.
            fields (list): The fields to be included in the form.
            widgets (dict): The widgets to be used for the fields.

        """
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
            'username',
            'phone_number',
            ]
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control','required':'True'}),
            'last_name': TextInput(attrs={'class': 'form-control','required':'True'}),
            'email': EmailInput(attrs={'class': 'form-control','required':'True'}),
            'password': PasswordInput(attrs={'class': 'form-control','required':'True'}),
            'username': TextInput(attrs={'class': 'form-control','required':'True'}),
            'phone_number': NumberInput(attrs={'class': 'form-control',}),
     
        }
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Password and Confirm Password does not match")
            
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email
            

        
class AboutForm(ModelForm):
    class Meta:
        model = User
        fields = ['about','facebook','instagram','snapchat']  
        widgets = {
            'about':TextInput(attrs={'class': 'form-control'}),
            'facebook':forms.URLInput(attrs={'class': 'form-control'}),
            'instagram':forms.URLInput(attrs={'class': 'form-control'}),
            'snapchat':forms.URLInput(attrs={'class': 'form-control'}),
        }    
        
        
class ProfileUpdateForm(RegistrationForm):
    password = None
    confirm_password = None


    
class UserProfileForm(ModelForm):
    class Meta:
        model = User
        fields = [
           
            'date_of_birth',
            'gender',
            'hobbies',
            'interest',
            'smoking_habits',
            'drinking_habits',
            'qualification',
            'profile_photo',
        ]  
        widgets = {
            
            'hobbies': Select(attrs={'class':'form-control'}),
            'interest': Select(attrs={'class':'form-control'}),
            'smoking_habits': Select(attrs={'class':'form-control'}),
            'drinking_habits': Select(attrs={'class':'form-control'}),
            'qualification': TextInput(attrs={'class':'form-control'}),
            'profile_photo': FileInput(),
            'date_of_birth': DateInput(attrs={'class': 'form-control','type' :'date'}),
            'gender': Select(attrs={'class': 'form-control'}),
        }
        
class UserUpdateForm(UserProfileForm):
    profile_photo = None
        
class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = [
            'address_line1',
            'address_line2',
            'city',
            'state',
            'zipcode',
            'country',
            
        ]  
        widgets = {
            'address_line1':TextInput(attrs={'class':'form-control'}),
            'address_line2':TextInput(attrs={'class':'form-control'}),
            'city': TextInput(attrs={'class':'form-control'}),
            'state': TextInput(attrs={'class':'form-control'}),
            'zipcode': TextInput(attrs={'class':'form-control'}),
            'country': Select(attrs={'class': 'form-control'}),
           
        }

    
        
        
class EmploymentForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'job_status',
            
            'company_name',
            'designation',
            'company_location',
            'job_title',
            'expertise_level'
            
        ]  
        widgets = {
            'job_status': Select(attrs={'class':'form-control'}),
            
            'company_name': TextInput(attrs={'class':'form-control'}),
            'designation': TextInput(attrs={'class':'form-control'}),
            'company_location': TextInput(attrs={'class':'form-control'}),
            'job_title': TextInput(attrs={'class':'form-control'}),
            'expertise_level': Select(attrs={'class': 'form-control'}),
           
        }

    
class FamilyForm(ModelForm):
    class Meta:
        model = Family
        fields =[
            'father_name',
            'father_occupation',
            'mother_name',
            'mother_occupation',
            'num_of_siblings',
            'marital_status',
            'religion',
            'caste',
            'family_values',
            'disability',
            'family_type',
            'family_class',
                
        ]
        widgets ={
            'father_name': TextInput(attrs={'class':'form-control'}),
            'father_occupation': TextInput(attrs={'class':'form-control'}),
            'mother_name': TextInput(attrs={'class':'form-control'}),
            'mother_occupation': TextInput(attrs={'class':'form-control'}),
            'num_of_siblings': NumberInput(attrs={'class':'form-control'}),
            'marital_status': Select(attrs={'class': 'form-control'}),
            'religion': Select(attrs={'class': 'form-control'}),
            'caste': Select(attrs={'class': 'form-control'}),
            'family_values': Select(attrs={'class': 'form-control'}),
            'disability': Select(attrs={'class': 'form-control'}),
            'family_type': Select(attrs={'class': 'form-control'}),
            'family_class': Select(attrs={'class': 'form-control'}),
            
            
            
        }
        
        
class PartnerForm(ModelForm):
    class Meta:
        model = Partner
        fields =[
            'height',
            'weight',
            'income',
            'horoscope',
            'from_weight',
            'to_weight',
            'from_height',
            'to_height',
            'from_age',
            'to_age',
            'caste',
            'religion',
            'min_income',
            'max_income',
                
        ]
        widgets ={
            'height': NumberInput(attrs={'class':'form-control','placeholder':'Enter your height in cm'}),
            'weight': NumberInput(attrs={'class':'form-control','placeholder':'Enter your weight in kg'}),
            'income': NumberInput(attrs={'class':'form-control','placeholder':'Enter your income'}),
            'horoscope': TextInput(attrs={'class':'form-control','placeholder':'Enter your horoscope'}),
            'from_weight': NumberInput(attrs={'class': 'form-control','placeholder':'Enter your partner min weight '}),
            'to_weight': NumberInput(attrs={'class': 'form-control','placeholder':'Enter your partner max weight'}),
            'from_height': NumberInput(attrs={'class': 'form-control','placeholder':'Enter your partner min height in cm'}),
            'to_height': NumberInput(attrs={'class': 'form-control','placeholder':'Enter your partner max height in cm'}),
            'from_age': NumberInput(attrs={'class': 'form-control','placeholder':'Enter your partner min age'}),
            'to_age': NumberInput(attrs={'class': 'form-control','placeholder':'Enter your partner max age'}),
            'caste': Select(attrs={'class': 'form-control','placeholder':'Enter your partner caste'}),
            'religion': Select(attrs={'class': 'form-control','placeholder':'Enter your partner relegion'}),
            'min_income': NumberInput(attrs={'class': 'form-control','placeholder':'Enter your partners min income'}),
            'max_income': NumberInput(attrs={'class': 'form-control','placeholder':'Enter your partners max income'}),
            
            
            
        }

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_photo']
        
class FriendRequestForm(ModelForm):
    class Meta:
        model = FriendRequest
        fields = ('to_user',)
        
class ShortlistForm(forms.ModelForm):
    class Meta:
        model = Shortlist
        fields = ['shortlisted_user']
        
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'content']
        
class CustomPasswordResetForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("No user is associated with this email address")
        return email