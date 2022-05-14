from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Plant(models.Model):
  name = models.CharField(max_length=256)
  sci_name = models.CharField(max_length=512, blank=True, default='Not recorded')
  description = models.TextField(default='Needs description', blank=True, null=True)
  img_url = models.URLField(max_length=512, blank=True, null=True)
  water_freq = models.CharField(max_length=50)
  water_qty = models.CharField(max_length=50, blank=True, default='normal')
  light_level = models.CharField(max_length=50, blank=True)
  temp = models.CharField(max_length=50, blank=True)
  humidity = models.CharField(max_length=50, blank=True, default='medium')
  fertilizer_type = models.CharField(max_length=256, blank=True)
  fertilizer_freq = models.CharField(max_length=50, blank=True)
  def __str__(self):
    return self.name


class User(AbstractUser):
  profile_img = models.CharField(max_length=512, blank=True, default="")
  pref_day1 = models.CharField(max_length=50, blank=True, default="")
  pref_day2 = models.CharField(max_length=50, blank=True, default="")
  plants = models.ManyToManyField(Plant, through='Houseplant')
  def __str__(self):
    return self.username

# class User(models.Model):
#   name = models.CharField(max_length=256)
#   email = models.EmailField(max_length=256, blank=True, null=True)
#   username = models.CharField(max_length=256)
#   password = models.CharField(max_length=1024)
#   profile_img = models.CharField(max_length=512, blank=True, null=True)
#   pref_day1 = models.CharField(max_length=50, blank=True, null=True)
#   pref_day2 = models.CharField(max_length=50, blank=True, null=True)
#   plants = models.ManyToManyField(Plant, through='Houseplant')
#   def __str__(self):
#     return self.name


class Location(models.Model):
  user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='locations')
  name = models.CharField(max_length=256)
  description = models.CharField(max_length=512)
  img_url = models.URLField(max_length=512, blank=True)
  light_level = models.CharField(max_length=50, blank=True)
  temp = models.CharField(max_length=50, blank=True)
  humidity = models.CharField(max_length=50, blank=True)
  notes = models.TextField(blank=True)
  plants = models.ManyToManyField(Plant, through='Houseplant')
  def __str__(self):
    return self.name
  

class Houseplant(models.Model):
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  plant_id = models.ForeignKey(Plant, on_delete=models.CASCADE)
  loc_id = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True)
  img_url = models.CharField(max_length=512, blank=True)
  notes = models.TextField(blank=True)
  date_created = models.DateTimeField(auto_now_add=True)
  date_modified = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ['-id'] # This returns the data ordered with newest at the top


