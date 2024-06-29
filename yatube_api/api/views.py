from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import permissions
from rest_framework import filters
from rest_framework import pagination
from django.shortcuts import get_object_or_404

from .permissions import IsAuthorOrReadOnly, ReadOnly
from .serializers import (CommentSerializer, FollowSerializer,
                          GroupSerializer, PostSerializer)
from posts.models import Comment, Follow, Group, Post, User


class ChoosePermissionMixin:
    """
    Промежуточный миксин.

    выбор пермишена в зависимости от типа запроса.
    """
    permission_classes = (IsAuthorOrReadOnly,)

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()


class PostViewSet(ChoosePermissionMixin, viewsets.ModelViewSet):
    """Вьюсет для модели Post."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = pagination.LimitOffsetPagination

    def perform_create(self, serializer):
        """Создание поста, где автор - текущий пользователь."""
        serializer.save(author=self.request.user)


class CommentViewSet(ChoosePermissionMixin, viewsets.ModelViewSet):
    """Вьюсет для модели Comment."""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_post(self):
        """Получение поста, соответствующего post_id из URL."""
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self):
        """Получение комментариев, связанных с полученным постом."""
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        """Создание комм-ия к текущему посту, где автор - текущий польз-ль."""
        serializer.save(author=self.request.user,
                        post=self.get_post())


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для модели Group."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CreateListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """Промежуточный вьюсет: создание записи и получение записей."""
    pass


class FollowViewSet(CreateListViewSet):
    """Вьюсет для модели Follow."""
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_user(self):
        """Получение объекта текущего юзера."""
        return get_object_or_404(User, username=self.request.user)

    def get_queryset(self):
        """Получение польз-ей, на которых подписан текущий юзер."""
        return self.get_user().users.all()

    def perform_create(self, serializer):
        """Создание записи о подписке для текущего пользователя."""
        serializer.save(user=self.get_user())
