from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from account.models import User

class UserCreateSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(
        max_length = 128,
        min_length = 4,
        write_only = True
        
    )
    
    token = serializers.CharField(max_length=255, read_only = True)
    
    class Meta:
        model = User
        fields = ['email', 'age', 'username', 'date_of_birth', 'password', 'token']
        
    def create(self, validated_data):   #create method
        return User.objects.create_user(**validated_data)