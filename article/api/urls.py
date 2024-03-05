from django.urls import path
from .views import (
    article_list,
    article_detail_update_delete_api_view,
    # article_detail_api_view,
    # tag_list,
)
app_name = 'api'

urlpatterns = [
    path('list/', article_list, name='list'),
    # path('detail/<int:pk>/', article_detail_api_view, name='detail'),
    # path('tag/', tag_list, name='tag'),
    path('detail-update-delete/<int:pk>/', article_detail_update_delete_api_view, name='detail-update-delete'),
]

