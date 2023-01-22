from rest_framework.viewsets import ModelViewSet

from .models import Client, Contract, Event
from .serializers import (
    ClientSerializer,
    ContractSerializer,
    EventSerializer,
)
from .permissions import (
    IsGroupSales, IsGroupSupport, IsManager
)


class ClientViewset(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [IsManager | IsGroupSales | IsGroupSupport]
        elif self.action == 'create':
            permission_classes = [IsManager | IsGroupSales]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsManager | IsGroupSales]
        elif self.action == 'destroy':
            permission_classes = [IsManager]
        return [permission() for permission in permission_classes]



class ContractViewset(ModelViewSet):
    serializer_class = ContractSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [IsManager | IsGroupSales | IsGroupSupport]
        elif self.action == 'create':
            permission_classes = [IsManager | IsGroupSales]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsManager | IsGroupSales]
        elif self.action == 'destroy':
            permission_classes = [IsManager]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        if self.request.user.role == "SUPPORT":
            return Contract.objects.filter(event__support_contact=self.request.user).order_by('date_created')
        elif self.request.user.role == "SALES":
            return Contract.objects.filter(client__sales_contact=self.request.user).order_by('date_created')
        return Contract.objects.all().order_by('date_created')


class EventViewset(ModelViewSet):
    serializer_class = EventSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'list' or self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsManager | IsGroupSales | IsGroupSupport]
        elif self.action == 'create':
            permission_classes = [IsManager | IsGroupSales]
        elif self.action == 'destroy':
            permission_classes = [IsManager]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        if self.request.user.role == "SUPPORT":
            return Event.objects.filter(support_contact=self.request.user).order_by('date_created')
        elif self.request.user.role == "SALES":
            return Event.objects.filter(contract__client__sales_contact=self.request.user).order_by('date_created')
        return Event.objects.all().order_by('date_created')
