from django.contrib import admin

<<<<<<< HEAD
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "role")
    empty_value_display = "-пусто-"



admin.site.register(User, UserAdmin)
=======
# Register your models here.
>>>>>>> d3737c12f4e6f58f7e54ef10e5bc580632cf75ab
