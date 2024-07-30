
# Create your models here.


from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime

class Hobby(models.Model):
    
    name = models.CharField(max_length=100,unique=True)
 
    def __str__(self):
        return self.name


class User(AbstractUser):
    # Add your custom fields here
    
    GENDER_CHOICES = (('Male','Male'),('Female','Female'),('Other','Other'),)
    INTEREST_CHOICES = (('Male','Male'),('Female','Female'),('Other','Other'),)
    EXPERTISE_CHOICES = (('Beginner','Beginner'),('Intermediate','Intermediate'),('Expert','Expert'),)
    JOB_STATUS_CHOICES = (('Employee','Employee'),('Employer','Employer'),('JobSeeker','JobSeeker'),)
    
    
    phone_number =models.CharField(
        max_length=15,
        blank=True,
        verbose_name='Phone Number'
    )
    
    profile_photo = models.ImageField(
        upload_to='profile_photos/', 
        blank=True, 
        verbose_name='Profile photo'
    )
    
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        verbose_name='Date Of Birth'
    )
    
    gender =models.CharField(
        max_length= 6,
        choices=GENDER_CHOICES,
        blank=True,
        verbose_name='Gender',
        default='Male'
         
    )
    
   
    
    friend = models.ManyToManyField('self', blank=True)
    hobbies = models.ForeignKey(Hobby,related_name='users',blank=True,null=True,on_delete=models.CASCADE)
    interest =models.CharField(max_length=6,choices=INTEREST_CHOICES,verbose_name='Interested In',blank=True,null=True,default='Male')
    smoking_habits = models.CharField(max_length=50, choices=[('yes', 'Yes'), ('no', 'No')], default='no',blank=True,null=True)
    drinking_habits = models.CharField(max_length=50, choices=[('yes', 'Yes'), ('no', 'No')], default='no',blank=True,null=True)
    qualification = models.CharField(max_length=255,blank=True,null=True)
    job_status = models.CharField(max_length=100,blank=True,verbose_name='Job Status',choices=JOB_STATUS_CHOICES)
    company_name = models.CharField(max_length=255, blank=True, null=True,verbose_name='Company Name')
    designation = models.CharField(max_length=100,blank=True,null=True,verbose_name='Designation')
    company_location = models.CharField(max_length=200,blank=True,null=True,verbose_name='Company Location')
    job_title = models.CharField(max_length=255, blank=True, null=True,verbose_name='Job Title')
    expertise_level = models.CharField(max_length=100,
        blank=True,
        verbose_name='Expertise Level',
        choices=EXPERTISE_CHOICES)
    about = models.TextField(max_length=1000,blank=True,null=True)
    facebook = models.URLField(max_length=100,blank=True,null=True)
    instagram = models.URLField(max_length=100,blank=True,null=True)
    snapchat = models.URLField(max_length=100,blank=True,null=True)
    
    
   
    


    @property
    def is_basic_profile_complete(self):
        """
        Determines if the basic profile is complete by checking all the fields.

        Returns:
            bool: True if the user has filled all the required fields, False otherwise.
        """
        
        return all([
            self.first_name,
            self.last_name,
            self.email,
            self.password,
            self.username,
            self.phone_number,
            self.profile_photo,
            self.date_of_birth,
            self.gender,
            self.hobbies,
            self.interest,
            self.smoking_habits,
            self.drinking_habits,
            self.job_status,
            self.company_name,
            self.designation,
            self.company_location,
            self.job_title,
            self.expertise_level,
            self.friend,
            
            
            
            
        ])
        
    @property
    def age(self):
        
        
        if self.date_of_birth is not None:
            return int((datetime.date.today()-self.date_of_birth).days / 365)
        else:
            return None
        
        
    def add_friend(self, profile):
        """
        Add a profile to this user's friends list.
        """
        self.friends.add(profile)
        self.save()

    def unfriend(self, profile):
        """
        Remove a profile from this user's friends list.
        """
        self.friend.remove(profile)
        self.save()
        
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Change this to a unique name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='custom_user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # Change this to a unique name
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='custom_user',
    )

class Image(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='images')
    
    
    def __str__(self):
        return f"Image {self.id} for {self.user.first_name}"
    
class Reel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='reels')
    reel = models.FileField(upload_to='reels/')
    
    
    def __str__(self):
        return f"Reel {self.id} for {self.user.first_name}"
    

    
  
class Address(models.Model):
    
        COUNTRY_CHOICES = (
        ('IN','INDIA'),
        )
    
        user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='address')
        address_line1 = models.TextField(
        max_length=100,
        blank=True,
        verbose_name='Address Line1',
        )
    
    
        address_line2 = models.TextField(
        max_length=100,
        blank=True,
        verbose_name='Address Line2',
        )
    
        city = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='City'
        
        )
    
        state = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='State'
        )
    
        zipcode = models.CharField(
        max_length=6,
        blank=True,
        verbose_name='Zip Code'
        )
    
    
        country = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Country',
        choices=COUNTRY_CHOICES
        ) 
        
        
        @property
        def is_address_profile_complete(self):
        
        
            return all([
                self.address_line1,
                self.address_line2,
                self.city,
                self.state,
                self.zipcode,
                self.country,
            
            
            
            
            
        ])
        

class FriendRequest(models.Model):
    from_user = models.ForeignKey(User,related_name="sent_requests",on_delete=models.CASCADE)
    to_user = models.ForeignKey(User,related_name="recieved_requests",on_delete=models.CASCADE)
    status = models.CharField(choices=[('pending','Pending'),('accepted','Accepted'),('rejected','Rejected')],default='pending',max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages', verbose_name='Sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages', verbose_name='Receiver')
    content = models.CharField(max_length=4000, verbose_name='Content')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')
    status = models.CharField(max_length=20, choices=[
        ('sent', 'Sent'),
        ('delivered','Delivered'),
        ('read', 'Read'),
    ], default='unread', verbose_name='Status')
    
    def __str__(self):
        return f"Message from {self.sender} to {self.receiver} at {self.timestamp}"
        
