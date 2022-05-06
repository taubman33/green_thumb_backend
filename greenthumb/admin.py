from django.contrib import admin
from .models import User, Plant, Location, Houseplant

# Register your models here.
admin.site.register(User)
admin.site.register(Location)
admin.site.register(Plant)
admin.site.register(Houseplant)