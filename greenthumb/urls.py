from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
  path('users/', views.UserList.as_view(), name='user_list'),
  path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
  path('plants/', views.PlantList.as_view(), name='plant_list'),
  path('plants/<int:pk>', views.PlantDetail.as_view(), name='plant_detail'),
  path('locations/', views.LocationList.as_view(), name='location_list'),
  path('locations/<int:pk>', views.LocationDetail.as_view(), name='location_detail'),
  path('houseplants/', views.HouseplantList.as_view(), name='houseplant_list'),
  path('houseplants/<int:pk>', views.HouseplantDetail.as_view(), name='houseplant_detail'),
]
