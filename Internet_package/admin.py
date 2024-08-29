from django.contrib import admin
from .models import internet
@admin.register(internet)
class internetAdmin(admin.ModelAdmin):
    pass