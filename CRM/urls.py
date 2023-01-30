from django.urls import path
from rest_framework import routers

from .views import (
    ClientViewset, ContractViewset, EventViewset
)

router = routers.DefaultRouter()
router.register('client', ClientViewset, basename='client')
router.register('contract', ContractViewset, basename='contract')
router.register('event', EventViewset, basename='event')

urlpatterns = [
]

urlpatterns += router.urls
