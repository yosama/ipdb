from builtins import isinstance

from rest_framework.permissions import BasePermission

class UserPermission(BasePermission):

    # User List: Solo  lo puede ver un usuario administrador (y por tanto autenticado)
    # Creacion de usuarios: Cualquier usuario
    # Detalle de usuario: Los admin puede ver cualquier usuario, usuarios autenticado(no admin) pueden ver sus datos, no autenticados no puede ver nada
    # Actualizacion de usuario: Los admin puede ver cualquier usuario, usuarios autenticado(no admin) pueden ver sus datos, no autenticados no puede ver nada
    # Borrado de usuario: Los admin puede ver cualquier usuario, usuarios autenticado(no admin) pueden ver sus datos, no autenticados no puede ver nada

    def has_permission(self, request, view):
        """
        Define si el usario puede ejecutar una accion (GET, POST, PUT, DELETE) sobre la vista 'view'
        :param request:
        :param view:
        :return:
        """
        from users.api import UserDetailAPI

        if request.method == "POST" or request.user.is_superuser:
            return True

        if request.user.is_authenticated and request.method == "GET" and isinstance(view, UserDetailAPI):
            return True

        return request.user.is_authenticated and (request.method == "PUT" or request.method == "DELETE")

    def has_object_permission(self, request, view, obj):
        """
        El usuario autenticado (request.user) solo puede trabajar con el usuario solicitado (obj) si es el mismo o un administrador
        :param request:
        :param view:
        :param obj:
        :return:
        """
        return request.user == obj or request.user.is_superuser
