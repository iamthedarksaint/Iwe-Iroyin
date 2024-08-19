from django.urls import path
from .views import (
    ArticleList, 
    ArticleUpdateView, 
    ArticleDetail, 
    ArticleDeleteView,
    ArticleCreateView,
    )

urlpatterns = [
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/', ArticleDetail.as_view(), name='article_detail'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('new/', ArticleCreateView.as_view(), name ='article_new'),
    path('', ArticleList.as_view(), name='article_list'),
]


