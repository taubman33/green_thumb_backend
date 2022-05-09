from rest_framework import serializers
from .models import User, Plant, Location, Houseplant

class PlantSerializer(serializers.ModelSerializer):

  class Meta:
    model = Plant
    fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
  plants = PlantSerializer(many=True, read_only=True)
  class Meta:
    model = User
    
    fields = [field.name for field in model._meta.fields]
    fields.append('plants')
    # fields = '__all__'
    # extra_fields = ['plants']
    
    # fields = ('id','name','email','username','password','profile_img','pref_day1','pref_day2','plants')


class LocationSerializer(serializers.ModelSerializer):
  plants = PlantSerializer(many=True, read_only=True)
  class Meta:
    model = Location
    fields = '__all__'
    extra_fields = ('plants')


class HouseplantSerializer(serializers.ModelSerializer):
  user = UserSerializer(read_only=True, source='user_id')
  plant = PlantSerializer(read_only=True, source='plant_id')
  location = LocationSerializer(read_only=True, source='loc_id')

  class Meta:
    model = Houseplant
    fields = '__all__'
    extra_fields = ('user','plant', 'location')


class UserAllDetailsSerializer(serializers.ModelSerializer):
  # houseplants = HouseplantSerializer(many = True, read_only = True)
  plants = PlantSerializer(many=True, read_only=True)
  locations = LocationSerializer(many=True, read_only=True)
  class Meta:
    model = User
    fields = "__all__"
    # extra_fields = ('locations', 'houseplants')
    extra_fields = ('locations', 'plants')