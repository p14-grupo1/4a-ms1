from django.urls import path
from .views import EmpresaListCreate, HotelListCreate, TuristaHotelRatingListCreate, TuristaListCreate
urlpatterns = [
    path('turista/', TuristaListCreate.as_view()),
    path('ratings/', TuristaHotelRatingListCreate.as_view()),
    path('empresa/', EmpresaListCreate.as_view()),
    path('hotel/', HotelListCreate.as_view()),
]
