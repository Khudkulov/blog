from django.shortcuts import redirect, get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from article.models import Article
from rest_framework.decorators import api_view, permission_classes
from .permissions import IsOwnerOrReadOnly
from .serializers import ArticleSerializer


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)



