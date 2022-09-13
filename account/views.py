from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from account.serializers import UserCreateSerializer, LoginSerializer

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
    