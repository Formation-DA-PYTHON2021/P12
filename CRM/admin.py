from django.contrib import admin
from .models import User, Client, Contract, Event

admin.site.register(User)
admin.site.register(Client)
admin.site.register(Contract)
admin.site.register(Event)
