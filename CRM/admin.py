from django.contrib import admin
from .models import User, Client, Contract, Event
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'role',
                    'is_active', 'is_staff', 'is_superuser',)
    search_fields = ['email']
    ordering = ['id']


admin.site.register(Client)
admin.site.register(Contract)
admin.site.register(Event)
