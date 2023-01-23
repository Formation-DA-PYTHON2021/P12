from django.contrib import admin
from .models import User, Client, Contract, Event
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'role',
                    'is_active', 'is_staff', 'is_superuser',)
    search_fields = ['email', 'first_name']
    ordering = ['id']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            'Client Info :',
            {'fields': ('last_name', 'first_name', 'email', 'phone', 'mobile', 'company_name')}),
        (
            'Sales Contact :',
            {'fields': ('sales_contact',)},
        ),
        ('File info', {'fields': ('date_created', 'date_updated')})
    )
    readonly_fields = ('date_created', 'date_updated')
    list_display = ('id', 'last_name', 'first_name', 'email', 'phone', 'mobile', 'company_name')
    search_fields = ['id', 'last_name', 'sales_contact']
    ordering = ['id']


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            'Contract Info :',
            {'fields': ('client', 'status', 'amount', 'payment_invoice', 'date_payment')}),
        (
            'Sales Contact :',
            {'fields': ('sales_contact',)},
        ),
        ('File info', {'fields': ('date_created', 'date_updated')})
    )
    readonly_fields = ('date_created', 'date_updated')
    list_display = ('id', 'client', 'sales_contact', 'status', 'payment_invoice', 'date_payment')
    search_fields = ['id', 'client__last_name', 'sales_contact']
    ordering = ['id']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            'Event Info :',
            {
                'fields': (
                    'event_name',
                    'event_place',
                    'contract',
                    'event_participants',
                    'event_date',
                    'event_status',
                    'event_notes',
                )}),
        (
            'Support Contact :',
            {'fields': ('support_contact',)},
        ),
        ('File info', {'fields': ('date_created', 'date_updated')})
    )
    readonly_fields = ('date_created', 'date_updated')
    list_display = ('id',
                    'event_name',
                    'event_place',
                    'contract',
                    'support_contact',
                    'event_participants',
                    'event_date',
                    'event_status',
                    'event_notes',
                    )
    search_fields = ['event_name', 'event_place', 'contract__client__last_name']
    ordering = ['id']