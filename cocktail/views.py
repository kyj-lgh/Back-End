from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView

from cocktail.models import Cocktail
from cocktail.serializers import CocktailSerializer

class CocktailAPIView(ListCreateAPIView):   #칵테일 리스트, 생성 API
    permission_classes=(AllowAny,)
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer
    
    # def post(self, request):
    #     serializer = CocktailCreateSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class CocktaildetailAPIView(RetrieveUpdateDestroyAPIView):      #수정, 삭제 API
    permission_classes=(AllowAny,)
    serializer_class = CocktailSerializer
    
    def get_queryset(self):
        return Cocktail.objects.filter(pk = self.kwargs["pk"])     #kwargs = pk 전달 용도