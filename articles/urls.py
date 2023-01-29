from django.urls import path
from .views import (
  ArticleListView,
  ArticleUpdateView,
  ArticleDetailView,
  ArticleDeleteView,
  ArticleCreateView
)

urlpatterns = [
  path('',ArticleListView.as_view(),name='article_list'),
  path('blog/<int:pk>/edit/',ArticleUpdateView.as_view(),name='article_edit'),
  path('blog/<int:pk>/delete/',ArticleDeleteView.as_view(),name='article_delete'),
  path('blog/<int:pk>/',ArticleDetailView.as_view(),name='article_detail'),
  path('new/',ArticleCreateView.as_view(),name='article_new')
]