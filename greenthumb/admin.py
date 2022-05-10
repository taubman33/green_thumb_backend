from django.contrib import admin
from .models import User, Plant, Location, Houseplant

class UserAdmin(admin.ModelAdmin):
  model = User

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Location)
admin.site.register(Plant)
admin.site.register(Houseplant)