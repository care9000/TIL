from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.article_create, name='article_create'),
    path('<int:article_pk>/detail', views.detail, name='detail'),
    path('<int:article_pk>/update', views.article_update, name='article_update'),
    path('<int:article_pk>/delete', views.article_delete, name='article_delete'),
    path('<int:article_pk>/comment_create', views.comment_create, name='comment_create'),
    path('<int:article_pk>/<int:comment_pk>/comment_delete', views.comment_delete, name='comment_delete'),
    ]