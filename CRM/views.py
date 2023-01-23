from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Client, Contract, Event
from .serializers import (
    ClientSerializer,
    ContractSerializer,
    EventSerializer,
)
from .permissions import (
    IsGroupSales, IsGroupSupport, IsManager
)
from .filters import (
    ClientFilter,
    ContractFilter,
    EventFilter
)


class ClientViewset(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_class = ClientFilter

    def get_permissions(self):
        permission_classes = []
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [IsAuthenticated, IsManager | IsGroupSales | IsGroupSupport]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated, IsManager | IsGroupSales]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAuthenticated, IsManager | IsGroupSales]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsManager]
        return [permission() for permission in permission_classes]


class ContractViewset(ModelViewSet):
    serializer_class = ContractSerializer
    filter_class = ContractFilter

    def get_permissions(self):
        permission_classes = []
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [IsAuthenticated, IsManager | IsGroupSales | IsGroupSupport]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated, IsManager | IsGroupSales]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAuthenticated, IsManager | IsGroupSales]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsManager]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        if self.request.user.role == "SUPPORT":
            return Contract.objects.filter(event__support_contact=self.request.user).order_by('date_created')
        elif self.request.user.role == "SALES":
            return Contract.objects.filter(client__sales_contact=self.request.user).order_by('date_created')
        return Contract.objects.all().order_by('date_created')


class EventViewset(ModelViewSet):
    serializer_class = EventSerializer
    filter_class = EventFilter

    def get_permissions(self):
        permission_classes = []
        if self.action == 'list' or self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAuthenticated, IsManager | IsGroupSales | IsGroupSupport]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated, IsManager | IsGroupSales]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsManager]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        if self.request.user.role == "SUPPORT":
            return Event.objects.filter(support_contact=self.request.user).order_by('date_created')
        elif self.request.user.role == "SALES":
            return Event.objects.filter(contract__client__sales_contact=self.request.user).order_by('date_created')
        return Event.objects.all().order_by('date_created')
