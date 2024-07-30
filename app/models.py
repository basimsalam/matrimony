from django.db import models

from accounts.models import User

# Create your models here.
class Religion(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Caste(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name





class Family(models.Model):
    MARITAL_CHOICES = (
        ('Single','Single'),('Married','Married'),('Widowed','Widowed'),('Divorced','Divorced'),
        )
    
    VALUES_CHOICES = (
        ('Orthodox','Orthodox'),('Traditional','Traditional'),('Moderate','Moderate'),('Liberal','Liberal'),
        )
    CLASS_CHOICES = (
        ('Lower CLass','Lower CLass'),('Middle Class','Middle Class'),('Upper Class','Upper Class'),
        )
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    father_name = models.CharField(max_length=100,blank=True,verbose_name='Father Name')
    father_occupation =models.CharField(max_length=100,blank=True,verbose_name='Father Occupation')
    mother_name = models.CharField(max_length=100,blank=True,verbose_name='Mother Name')
    mother_occupation =models.CharField(max_length=100,blank=True,verbose_name='Mother Occupation')
    num_of_siblings =models.IntegerField(blank=True,verbose_name='Number Of Siblings')
    marital_status = models.CharField(max_length=100,blank=True,verbose_name='Marital Status',choices=MARITAL_CHOICES)
    religion = models.ForeignKey(Religion,on_delete=models.CASCADE,blank=True,null=True)
    caste = models.ForeignKey(Caste,on_delete=models.CASCADE,blank=True,null=True)
    family_values = models.CharField(max_length=100,blank=True,choices=VALUES_CHOICES)
    disability = models.CharField(max_length=50, choices=[('yes', 'Yes'), ('no', 'No')], default='no',blank=True,null=True)
    family_type = models.CharField(max_length=50, choices=[('Joint', 'Joint'), ('Nuclear', 'Nuclear')], blank=True,null=True)
    family_class = models.CharField(max_length=100,choices=CLASS_CHOICES)
    
    def __str__(self):
        return f"Family:{self.user.username},Religion:{self.religion},Caste:{self.caste}"
    
    def __str__(self):
        return all([
            self.father_name,
            self.father_occupation,
            self.mother_name,
            self.mother_occupation,
            self.num_of_siblings,
            self.marital_status,
            self.religion,
            self.caste,
            self.disability,
            self.family_type,
            self.family_class,
            self.family_values
        ])

class Partner(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    height = models.IntegerField(blank=True,null=True)
    weight = models.IntegerField(blank=True,null=True)
    income = models.CharField(max_length=100,blank=True)
    horoscope = models.CharField(max_length=100,blank=True)
    from_height = models.IntegerField(blank=True,null=True)
    to_height =models.IntegerField(blank=True,null=True)
    from_age =models.IntegerField(null=True,blank=True)
    to_age = models.IntegerField(null=True,blank=True)
    from_weight = models.IntegerField(blank=True,null=True)
    to_weight = models.IntegerField(blank=True,null=True)
    caste = models.ForeignKey(Caste,on_delete=models.CASCADE,blank=True,null=True)
    religion = models.ForeignKey(Religion,on_delete=models.CASCADE,blank=True,null=True)
    min_income = models.IntegerField(blank=True,null=True)
    max_income = models.IntegerField(blank=True,null=True)
    
    
    def __str__(self):
        return f"Partner:{self.user.username},Relegion:{self.religion},Caste:{self.caste}"
    
    def __str__(self):
        return all([
            self.height,
            self.weight,
            self.income,
            self.horoscope,
            self.from_height,
            self.to_height,
            self.from_age,
            self.to_age,
            self.from_weight,
            self.to_weight,
            
            self.min_income,
            self.max_income,
        ])
        
class Shortlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shortlister')
    shortlisted_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shortlisted')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'shortlisted_user')

    def __str__(self):
        return f'{self.user.username} shortlisted {self.shortlisted_user.username}'