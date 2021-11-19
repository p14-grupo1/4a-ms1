from rest_framework import serializers
from turismo.models import Empresa, Hotel, Turista, TuristaHotelRating

class EmpresaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Empresa
    fields = "__all__"

class HotelSerializer(serializers.ModelSerializer):
  # owner = EmpresaSerializer(read_only=True)
  class  Meta:
    model = Hotel
    fields = ['owner', 'type', 'address', 'name', 'qualification']
    
class TuristaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Turista
    fields = "__all__"
    
class TuristaHotelRatingSerializer(serializers.ModelSerializer):
  class Meta:
    model = TuristaHotelRating
    fields = "__all__"