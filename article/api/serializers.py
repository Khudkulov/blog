from rest_framework import serializers
from article.models import Article
from rest_framework.validators import ValidationError
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', "last_login", "date_joined"]


class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'author', 'name', 'image', 'created_date']

    def validate(self, attrs):
        exp = {}
        title = attrs.get('title')
        content = attrs.get('title')
        if not title[0].isupper():
            exp['title'] = []
            exp["title"].append("Title must be capitalize")
        if not content[0].isupper():
            exp["content"] = "Content must be capitalize"
        # if self.Meta.model.objects.filter(title=title).exists():
        #     exp['title'].append('title already exist')
        if exp:
            raise ValidationError(exp)
        return attrs

    def create(self, validated_data):
        user_id = self.context['user_id']
        validated_data['author_id'] = user_id
        print(user_id)
        return super().create(validated_data)


class ArticlePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['id', 'author', 'name', 'image', 'created_date']
