from rest_framework import serializers
from article.models import Article, Author, Content, Tag, Category, Comment
from rest_framework.validators import ValidationError
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class ArticleCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ArticleTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ArticleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ArticleContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'content', 'checkbox']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', "last_login", "date_joined"]


class AuthorUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'user', 'image', 'bio']


class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorUserSerializer(read_only=True)
    contents = ArticleContentSerializer(read_only=True, many=True)
    category = ArticleCategorySerializer(read_only=True)
    tags = ArticleTagSerializer(read_only=True, many=True)
    comments = ArticleCommentSerializer(read_only=True, many=True)

    class Meta:
        model = Article
        fields = ['id', 'author', 'name', 'image', 'contents', 'created_date', 'tags', 'category', 'comments']

    def validate(self, attrs):
        exp = {}
        name = attrs.get('name')
        # content = attrs.get('name')
        if not name[0].isupper():
            exp['name'] = []
            exp["name"].append("Title must be capitalize")
        # if not content[0].isupper():
        #     exp["content"] = "Content must be capitalize"
        # if self.Meta.model.objects.filter(title=title).exists():
        #     exp['title'].append('title already exist')
        if exp:
            raise ValidationError(exp)
        return attrs

    def create(self, validated_data):
        user_id = self.context['user_id']
        author = get_object_or_404(Author, user_id=user_id)
        validated_data['author'] = author
        return super().create(validated_data)


# class ArticlePostSerializer(serializers.ModelSerializer):
#     author = UserSerializer()
#
#     class Meta:
#         model = Article
#         fields = ['id', 'author', 'name', 'image', 'created_date']




