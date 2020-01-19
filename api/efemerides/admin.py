from django.contrib import admin
from .models import Efemerides

@admin.register(Efemerides)
class Efemerides(admin.ModelAdmin):
    pass
