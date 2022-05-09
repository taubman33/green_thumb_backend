from rest_framework import generics
from .serializers import UserSerializer, PlantSerializer, LocationSerializer, HouseplantSerializer, UserAllDetailsSerializer
from .models import User, Plant, Location, Houseplant
# from rest_framework.permissions import IsAdminUser, DjangoModelPermissionsOrAnonReadOnly

# Create your views here.
class UserList(generics.ListCreateAPIView):
  # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
  queryset = User.objects.all()
  serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class UserAllDetailsList(generics.ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserAllDetailsSerializer

class UserAllDetailsDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = User.objects.all()
  serializer_class = UserAllDetailsSerializer


class PlantList(generics.ListCreateAPIView):
  queryset = Plant.objects.all()
  serializer_class = PlantSerializer

class PlantDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Plant.objects.all()
  serializer_class = PlantSerializer


class LocationList(generics.ListCreateAPIView):
  queryset = Location.objects.all()
  serializer_class = LocationSerializer

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Location.objects.all()
  serializer_class = LocationSerializer


class HouseplantList(generics.ListCreateAPIView):
  queryset = Houseplant.objects.all()
  serializer_class = HouseplantSerializer

class HouseplantDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Houseplant.objects.all()
  serializer_class = HouseplantSerializer