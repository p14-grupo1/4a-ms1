from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Empresa(models.Model):
  SMALL = 'S'
  MEDIUM = 'M'
  BIG = 'B'
  SIZE_CHOICES = [
    (SMALL, 'Small'),
    (MEDIUM, 'Medium'), 
    (BIG, 'Big')
    ]
  nit = models.IntegerField()
  name = models.CharField(max_length=255)
  size = models.CharField(max_length=2, choices=SIZE_CHOICES, default=SMALL)\
    
  def __str__(self) -> str:
      return self.name

class Hotel(models.Model):
  HOTEL = 'H'
  MOTEL = 'M'
  RESORT = 'R'
  BOUTIQUE = 'B'
  GASTRONOMIC = 'G'
  TYPE_CHOICES = [
    (HOTEL, 'Hotel'),
    (MOTEL, 'Motel'), 
    (RESORT, 'Resort'), 
    (BOUTIQUE, 'Boutique'), 
    (GASTRONOMIC, 'Gastronomic')
  ]
  ONE = 1
  TWO = 2
  THREE = 3
  FOUR = 4
  FIVE = 5
  CHOICES = [
    (ONE, '1'),
    (TWO, '2'),
    (THREE, '3'),
    (FOUR, '4'),
    (FIVE, '5')
  ]
  name = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  type = models.CharField(max_length=2, choices=TYPE_CHOICES, default=HOTEL)
  qualification = models.PositiveSmallIntegerField(choices=CHOICES, default=1)
  owner = models.ForeignKey(Empresa, on_delete=models.PROTECT)
  
  def __str__(self) -> str:
      return self.name

class Turista(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  age = models.PositiveSmallIntegerField()
  name = models.CharField(max_length=255)
  
  def __str__(self) -> str:
      return self.name

class TuristaHotelRating(models.Model):
  ONE = 1
  TWO = 2
  THREE = 3
  FOUR = 4
  FIVE = 5
  CHOICES = [
    (ONE, '1'),
    (TWO, '2'),
    (THREE, '3'),
    (FOUR, '4'),
    (FIVE, '5')
  ]
  rating = models.PositiveSmallIntegerField(choices=CHOICES, default=FIVE)
  hotel = models.ForeignKey(Hotel, on_delete = models.CASCADE)
  tourist = models.ForeignKey(Turista, on_delete = models.CASCADE)