from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class User_info(models.Model):
    user_name=models.CharField(null=False,max_length=30)
    phone_number=models.IntegerField(null=False)
    password=models.CharField(max_length=50)
    email_address=models.EmailField(blank=True)
    
    def __str__(self):
        return self.user_name

class Contact_info(models.Model):
    user_id=models.ForeignKey(User_info,on_delete=models.CASCADE)
    contact_name=models.CharField(blank=False,max_length=30)
    contact_phone_number=models.IntegerField(blank=False)
    is_spam=models.BooleanField(default=False)
    
    def __str__(self):
        return self.contact_name
    
    
    def email(self):
        return None
     