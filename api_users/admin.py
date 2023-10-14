from django.contrib import admin

# Register your models here.
from .models import NewUser


# Register your models here.
@admin.register(NewUser)
class NewUserAdmin(admin.ModelAdmin):
    pass

