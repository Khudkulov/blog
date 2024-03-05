from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from article.models import Article, Tag
from rest_framework.decorators import api_view, permission_classes
from .permissions import IsOwnerOrReadOnly
from .serializers import ArticleSerializer, ArticleTagSerializer


# @api_view(['GET'])
# def tag_list(request):
#     tags = Tag.objects.all()
#     serializer = ArticleTagSerializer(tags, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def article_list(request):
    if request.method == "POST":
        context = {
            "user_id": request.user.id
        }
        serializer = ArticleSerializer(data=request.data, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        response = {
            "error": serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


# @api_view(['GET'])
# def article_detail_api_view(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     serializer = ArticleSerializer(article)
#     return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def article_detail_update_delete_api_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        if article.author.user.username == request.user.username:
            if request.method == 'DELETE':
                article.delete()
                return Response({"success": True, "message": "Article Deleted"}, status=status.HTTP_204_NO_CONTENT)
            else:
                data = request.data
                partial = False
                if request.method == "PATCH":
                    partial = True
                serializer = ArticleSerializer(data=data, partial=partial, instance=article)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"success": False, "message": "not token user"}, status=status.HTTP_401_UNAUTHORIZED)
