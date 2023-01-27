import django_filters

from .models import Client, Contract, Event


class ClientFilter(django_filters.FilterSet):
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Client
        fields = []


class ContractFilter(django_filters.FilterSet):
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='iexact')
    date_created = django_filters.CharFilter(lookup_expr='icontains')
    amount = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        Model = Contract
        fields = []


class EventFilter(django_filters.FilterSet):
    event_date = django_filters.CharFilter(lookup_expr='icontains')
    event_place = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='iexact')
    email = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        Model = Event
        fields = []
