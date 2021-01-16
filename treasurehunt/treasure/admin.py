
from django.contrib import admin
from .models import Treasure

# Register your models here.
@admin.register(Treasure)
class TreasureAdmin(admin.ModelAdmin):
    list_display = ("hider","latitude","longitude")