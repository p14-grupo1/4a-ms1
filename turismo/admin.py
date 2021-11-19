from django.contrib import admin
from .models import Empresa, Hotel, Turista, TuristaHotelRating
# Register your models here.
admin.site.register(Turista)
admin.site.register(Empresa)
admin.site.register(TuristaHotelRating)
admin.site.register(Hotel)