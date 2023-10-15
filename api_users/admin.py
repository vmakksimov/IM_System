from django.contrib import admin

from api_users.models import CustomModelUser


# Register your models here.
@admin.register(CustomModelUser)
class CustomModelUserAdmin(admin.ModelAdmin):
    pass