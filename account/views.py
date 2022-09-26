from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView
from rest_framework.views import APIView
from account.models import User

from account.serializers import UserCreateSerializer, LoginSerializer, UserListSerializer, UserUpdateSerializer

class UserCreateAPIView(APIView):
    permission_classes = (AllowAny,)    
    #permission_classes = 누가 이 view를 사용 가능한지에 대한 범위를 결정
    # 사용자 등록은 누가나 가능해야 하기때문에 AllowAny로 설정
    serializer_class = UserCreateSerializer
    
    def post(self, request):
        user = request.data     #요청한 데이터를 받아오기        
        serializer = self.serializer_class(data=user)       #직렬화
        serializer.is_valid(raise_exception=True)   #유효성 확인
        serializer.save()   #저장
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        #직렬화된 데이터를 반환
        
class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_classes = LoginSerializer
    
    def post(self, request):
        user = request.data     #요청한 데이터를 받아오기        
        serializer = self.serializer_classes(data=user)       #직렬화
        serializer.is_valid(raise_exception=True)   #유효성 확인
    
        return Response(serializer.data, status = status.HTTP_200_OK)
    
class UserRetrieveUpdateView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated, )  #로그인한 사용자만 접근 가능
    serializer_class = UserUpdateSerializer
    
    def get(self,request, *args, **kwargs):     #RetiveUpdateAPIView에서 제공하는 get method
        serializer = self.serializer_class(request.user)    #User 객체를 client에게 보내주기 위한 serializer
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def patch(self, request, *args, **kwargs):
        serializer_data = request.data
        
        serializer = self.serializer_class(
            request.user, data = serializer_data, partial=True  
            #request.user가 instance, validated_data가 serializer_data, 
            #partial=True는 부분 업데이트가 가능하도록 하는 옵션
        )
        
        serializer.is_valid(raise_exception=True)
        
        serializer.save()   #업데이트된 사용자의 정보를 DB에 저장
        
        return Response(serializer.data, status = status.HTTP_200_OK)
    
class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer