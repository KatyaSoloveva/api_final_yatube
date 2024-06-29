from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post, User


class AuthorMixin(serializers.ModelSerializer):
    """Миксин для поля автора."""

    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)


class PostSerializer(AuthorMixin, serializers.ModelSerializer):
    """Сериализатор для модели Post."""

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(AuthorMixin, serializers.ModelSerializer):
    """Сериализатор для модели Comment."""

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Group."""

    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Follow."""

    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault())
    following = serializers.SlugRelatedField(slug_field='username',
                                             queryset=User.objects.all())

    class Meta:
        fields = '__all__'
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            )
        ]

    def validate(self, data):
        """Проверка на то, что польз-ль не подпишется на себя."""
        if data['following'] == self.context['request'].user:
            raise serializers.ValidationError(
                'Нельзя оформить подписку на самого себя!')
        return data
