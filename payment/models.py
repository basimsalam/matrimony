from django.db import models

from django.conf import settings

from accounts.models import User

# Create your models here.

class Plan(models.Model):
    name = models.CharField(max_length=50)
    stripe_plan_id = models.CharField(max_length=100, default='default_plan_id')
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    duration = models.IntegerField(default=30,help_text="Duration in days")

    def __str__(self):
        return self.name
    
    
class UserSubscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.plan.name}"