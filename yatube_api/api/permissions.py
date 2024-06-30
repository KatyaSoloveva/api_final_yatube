from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Kастомный класс-permission.

    Пользователю, не прошедшему проверку, разрешен доступ только на чтение.
    """

    def has_object_permission(self, request, view, obj):
        """Проверка: польз-ль - автор объекта класса/запраш-ый метод без-ный"""
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
