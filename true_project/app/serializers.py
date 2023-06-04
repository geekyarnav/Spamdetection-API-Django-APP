from rest_framework import serializers
from .models import User_info,Contact_info

class Contact_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact_info
        fields= ('user_id', 'contact_name', 'contact_phone_number', 'is_spam', 'email')
        
        
class User_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model=User_info
        fields="__all__"