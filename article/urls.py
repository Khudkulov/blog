from django.urls import path, include
from .views import (
    list_articles_view,
    detail_articles_view,

)
app_name = 'article'

urlpatterns = [
    path('list/', list_articles_view, name='list_articles'),
    path('detail/<slug:slug>/', detail_articles_view, name='detail_articles'),
    path('api/', include('article.api.urls', namespace='api')),

]
