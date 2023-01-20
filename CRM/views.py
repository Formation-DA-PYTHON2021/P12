from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated


from .models import Client, Contract, User, Event
from .serializers import (
    UserSerializer,
    ClientSerializer,
    SignupSerializer,
    ContractSerializer,
    EventSerializer,

)
from .permissions import (
    IsReadOnly, IsGroupSalesEditOnly, IsGroupSupportEditOnly, IsManager
)


class SignupViewset(GenericAPIView):
    serializer_class = SignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(
                    user,
                    context=self.get_serializer_context()).data
            }
        )


class ClientViewset(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, IsReadOnly, IsGroupSalesEditOnly, IsManager]

    """def post(self, request, *args, **kwargs):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            if serializer.validated_data["status"] is True:
                serializer.validated_data["sales_contact"] = request.user
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        client = self.get_object()
        serializer = ClientSerializer(data=request.data, instance=client)
        if serializer.is_valid(raise_exception=True):
            if serializer.validated_data["status"] is True:
                serializer.validated_data["sales_contact"] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)"""


class ContractViewset(ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, IsReadOnly, IsGroupSalesEditOnly, IsManager]


class EventViewset(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsReadOnly, IsGroupSalesEditOnly, IsGroupSupportEditOnly, IsManager]