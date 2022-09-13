from rest_framework import serializers
from account.models import User
from django.contrib.auth import authenticate
from django.utils import timezone

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
    
class LoginSerializer(serializers.Serializer):
    
    email = serializers.EmailField()
    username = serializers.CharField(max_length = 255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)   #입력을 받더라도 반환값으로 출력하지 않기 때문에 write_only
    last_login = serializers.CharField(max_length=255, read_only=True)  #입력을 받지 않기 때문에 read_only
    
    def validate(self, data):   #LoginSerializer의 인스턴스가 유효한지 확인
        email = data.get('email', None)
        password = data.get('password', None)
        
        if email is None:  
            raise serializers.ValidationError('Email Address is required to Login')
        
        if password is None:
            raise serializers.ValidationError('Password is required to Login')
        
        user = authenticate(username = email, password = password)
        # 받아온 email과 password를 데이터베이스에 있는 email과 password와 매칭
        
        if user is None:
            raise serializers.ValidationError('User with this email and password was not found')
        
        if not user.is_active:
            raise serializers.ValidationError('This user has been deactivated')
        
        user.last_login = timezone.now()
        user.save(update_fields = ['last_login'])
        
        return {'email' : user.email, 'username' : user.username, 'last_login' : user.last_login}