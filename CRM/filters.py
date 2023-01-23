from django_filters import rest_framework as filters

from .models import Client, Contract, Event


class ClientFilter(filters.FilterSet):
    last_name = filters.CharFilter(field_name='last_name', lookup_expr='icontains')
    email = filters.CharFilter(field_name='email', lookup_expr='iexact')

    class Meta:
        model = Client
        fields = ['last_name', 'email']


class ContractFilter(filters.FilterSet):
    client_last_name = filters.CharFilter(field_name='client__last_name', lookup_expr='icontains')
    client_email = filters.CharFilter(field_name='client__email', lookup_expr='iexact')
    date_created = filters.CharFilter(field_name='date_created', lookup_expr='icontains')
    amount__gt = filters.NumberFilter(field_name='amount', lookup_expr='gt')

    class Meta:
        Model = Contract
        fields = ['client_last_name', 'client_email', 'date_created', 'amount__gt']


class EventFilter(filters.FilterSet):
    event_date = filters.CharFilter(field_name='event_date', lookup_expr='icontains')
    event_place = filters.CharFilter(field_name='event_place', lookup_expr='icontains')
    client_last_name = filters.CharFilter(field_name='contract__client__last_name', lookup_expr='iexact')
    client_email = filters.CharFilter(field_name='contract__client__email', lookup_expr='iexact')

    class Meta:
        Model = Event
        fields = ['event_date', 'event_place', 'client_last_name', 'client_email']
