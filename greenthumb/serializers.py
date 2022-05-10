from rest_framework import serializers
from .models import User, Plant, Location, Houseplant
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class PlantSerializer(serializers.ModelSerializer):
  class Meta:
    model = Plant
    fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
  plants = PlantSerializer(many=True, read_only=True)

  # NEW AS OF AUTH SETUP
  email = serializers.EmailField(required=True)
  first_name = serializers.CharField()
  last_name = serializers.CharField()
  username = serializers.CharField(required=True)
  password = serializers.CharField(min_length=8, write_only=True)

  class Meta:
    model = User
    fields = ['id','email','first_name','last_name','username','password','profile_img','pref_day1','pref_day2']
    ## OLD 
    # fields = [field.name for field in model._meta.fields]
    fields.append('plants')

    ## NEW AS OF AUTH SETUP
    extra_kwargs = {'write_only': True}

  def create(self, validated_data):
    password = validated_data.pop('password', None)
    instance = self.Meta.model(**validated_data)
    if password is not None:
        instance.set_password(password)
    instance.save()
    return instance


    ## VERY OLD OLD
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