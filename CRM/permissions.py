from rest_framework import permissions


class IsManager(permissions.BasePermission):
   
    """
    Group MANAGEMENT : can CRUD
    """

    def has_permission(self, request, view):
        return (
            request.user.role == "MANAGEMENT"
            and request.method in permissions.SAFE_METHODS
        )

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class IsReadOnly(permissions.BasePermission):

    """
    All members must have read-only access to all clients, contracts or events.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser == True

    def has_permission(self, request, view):
        return True


class IsGroupSalesEditOnly(permissions.BasePermission):

    """
    A right of modification/access for :
    Sales group: all customers for whom they are responsible, as well as for their contracts and events.
    """

    def has_object_permission(self, request, view, obj):

        if request.method == "POST" | "PUT" and request.user.role == "SALES":
            return True
        return request.user.is_superuser == True

    def has_permission(self, request, view):
        return True


class IsGroupSupportEditOnly(permissions.BasePermission):

    """
    A right of modification/access for Support group: for all events for which they are responsible.
    """

    def has_object_permission(self, request, view, obj):

        if request.method == "POST" | "PUT" and request.user.role == "SUPPORT":
            return True
        return request.user.is_superuser == True

    def has_permission(self, request, view):
        return True