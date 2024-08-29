from django.contrib import admin
from .models import costomer,provider
@admin.register(costomer)
class ModelNameAdmin(admin.ModelAdmin):
    pass

@admin.register(provider)
class providerAdmin(admin.ModelAdmin):
    pass