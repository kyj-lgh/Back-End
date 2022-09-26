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
    
class UserUpdateSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField (
        max_length = 128,
        min_length = 4,
        write_only = True
    )
    
    class Meta:
        model = User
        fields = ['email', 'age', 'username', 'date_of_birth', 'password', 'token']
        
        read_only_fields = ('toekn',)   #read_only_fields = read_only = True와 같은 역할
        #token 필드는 속성값 지정이 없기 때문에 read_only_fields 사용
        
    def update(self,instance, validated_data):      #사용자의 정보를 업데이트 할 때 실행
        password = validated_data.pop('password', None)     #pop 함수를 이용해 password 제거
        
        for(key, value) in validated_data.items():
            setattr(instance, key, value)   #setattr(객체, 속성명, 속성값) - 정의된 속성값을  바꾸거나 새롭게 속성을 추가할 때 사용
            # instance 안에 있는 key의 값을 바꿔줌 - User의 속성값을 변경
            
        if password is not None:
            instance.set_password(password)
            
        instance.save()     #instance에 저장 DB에 저장되지는 않음 DB 저장을 view에서 진행
        
        return instance

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'age', 'date_of_birth', 'token']
        