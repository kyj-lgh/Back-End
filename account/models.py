from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)
from django.conf import settings
import jwt
from datetime import datetime, timedelta

class UserManager(BaseUserManager):
    def create_user(self, email, age, username, date_of_birth, password=None):
        '''
        주어진 이메일, 나이, 이름, 생일로 User 인스턴스 생성
        '''
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            age = age,
            username = username,
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, age, username, date_of_birth, password):
        '''
        주어진 이메일, 생일, 비밀번호로 User 인스턴스 생성
        최상위 사용자이기 때문에 권한 부여
        '''
        user = self.create_user(
            email,
            password=password,
            age = age,
            username = username, 
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    age = models.DecimalField(max_digits=200, decimal_places=0, blank = True)
    username = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth', 'age', 'username']

    def __str__(self):
        return self.email

    #True를 반환하여 권한이 있음을 알린다. Object를 반환하는 경우 사용 권한을 확인하는 절차가 필요
    def has_perm(self, perm, obj=None):
        return True

    #True를 반환하여 주어진 앱의 모델에 접근 가능하도록 한다.
    def has_module_perms(self, app_label):
        return True

    #True가 반환되면 관리자 화면 로그인 가능
    @property
    def is_staff(self):
        return self.is_admin
    
    @property
    def token(self):
        return self._generate_jwt_token()
    
    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days = 60)
        
        token = jwt.encode({
            'id' : self.pk,
            'exp' : dt.utcfromtimestamp(dt.timestamp())
        }, settings.SECRET_KET, algorithm = 'HS256')
    
        return token
