from rest_framework import permissions

from .models import Client, Contract, Event


class IsManager(permissions.BasePermission):
    """
    Group MANAGEMENT : can CRUD
    """

    def has_permission(self, request, view):
        if request.user and bool(request.user.role == "MANAGEMENT"):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return True


class IsGroupSales(permissions.BasePermission):
    """
    A right of modification/access for :
    Sales group: all customers for whom they are responsible, as well as for their contracts and events.
    """

    def has_permission(self, request, view):
        if request.user and bool(request.user.role == 'SALES'):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if type(obj) == Contract or type(obj) == Client or type(obj) == Event:
            if view.action in ['update', 'partial_update', 'retrieve', 'list']:
                return True
            if view.action == 'destroy':
                return False


class IsGroupSupport(permissions.BasePermission):
    """
    A right of modification/access for Support group: for all events for which they are responsible.
    """

    def has_permission(self, request, view):
        if request.user and bool(request.user.role == 'SUPPORT'):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if type(obj) == Contract:
            if view.action in ['list', 'retrieve']:
                return True
            if view.action in ['update', 'create', 'partial_update', 'destroy']:
                return False
        if type(obj) == Client:
            if view.action in ['list', 'retrieve']:
                return True
            if view.action in ['update', 'create', 'partial_update', 'destroy']:
                return False
        if type(obj) == Event:
            if view.action in ['update', 'partial_update', 'retrieve', 'list']:
                return True
            if view.action == 'destroy':
                return False
