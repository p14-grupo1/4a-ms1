from django.shortcuts import render
from rest_framework import generics, authentication, permissions, status
from turismo.models import Empresa, Hotel, Turista, TuristaHotelRating
from turismo.serializers import EmpresaSerializer, HotelSerializer, TuristaHotelRatingSerializer, TuristaSerializer
# Create your views here.
class HotelListCreate(generics.ListCreateAPIView):
  queryset = Hotel.objects.all()
  serializer_class = HotelSerializer

class EmpresaListCreate(generics.ListCreateAPIView):
  queryset = Empresa.objects.all()
  serializer_class = EmpresaSerializer
  
class TuristaHotelRatingListCreate(generics.ListCreateAPIView):
  queryset = TuristaHotelRating.objects.all()
  serializer_class = TuristaHotelRatingSerializer
  authentication_classes = [authentication.TokenAuthentication]
  permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
  
class TuristaListCreate(generics.ListCreateAPIView):
  queryset = Turista.objects.all()
  serializer_class = TuristaSerializer