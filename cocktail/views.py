from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView
from rest_framework.views import APIView

from cocktail.models import Cocktail
from cocktail.serializers import CocktailListSerializer, CocktailCreateSerializer

class CocktailListAPIView(ListAPIView):
    permission_classes=(AllowAny,)
    queryset = Cocktail.objects.all()
    serializer_class = CocktailListSerializer
    
class CocktailCreateAPIView(APIView):
    permission_classes=(AllowAny,)
    
    def post(self, request):
        serializer = CocktailCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
