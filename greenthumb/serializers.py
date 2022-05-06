from rest_framework import serializers
from .models import User, Plant, Location, Houseplant

class UserSerializer(serializers.ModelSerializer):
  # plants = serializers.RelatedField(
  #   view_name = 'user_detail',
  #   many = True,
  #   read_only = True
  # )
  class Meta:
    model = User
    fields = '__all__'
    # extra_fields = ()


class PlantSerializer(serializers.ModelSerializer):
  # plants = serializers.RelatedField(
  #   view_name = 'plant_detail',
  #   many = True,
  #   read_only = True
  # )
  class Meta:
    model = Plant
    fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
  # locations = serializers.HyperlinkedRelatedField(
  #   view_name = 'location_detail',
  #   many = True,
  #   read_only = True
  # )
  class Meta:
    model = Location
    fields = '__all__'

class HouseplantSerializer(serializers.ModelSerializer):
  user = UserSerializer(read_only=True, source = 'user_id')

  plant = serializers.StringRelatedField(
    # many=True,
    # queryset = Plant.objects.all(),
    source = 'plant_id'
  )

  class Meta:
    model = Houseplant
    fields = '__all__'
    extra_fields = ('user','plant')