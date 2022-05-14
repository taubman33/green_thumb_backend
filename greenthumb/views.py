from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User, Plant, Location, Houseplant
from .serializers import UserSerializer, PlantSerializer, LocationSerializer, HouseplantSerializer, UserAllDetailsSerializer
# from rest_framework.permissions import IsAdminUser, DjangoModelPermissionsOrAnonReadOnly

# Create your views here.

class UserList(APIView):
  def get(self, request):
    users = User.objects.all()
    return Response(users)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # lookup_field = 'id'

class UserDetailByUsername(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
  
class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogout(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        
        refresh_token = request.data['refresh_token']
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response(status=status.HTTP_205_RESET_CONTENT)



# class UserList(generics.ListCreateAPIView):
#   # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
#   queryset = User.objects.all()
#   serializer_class = UserSerializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#   queryset = User.objects.all()
#   serializer_class = UserSerializer

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