from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:article_pk>/edit/', views.edit, name='edit'),
    path('<int:article_pk>/detail/', views.detail, name='detail'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    path('<int:article_pk>/comment_create/', views.comment_create, name='comment_create'),
    path('<int:article_pk>/comment_delete/<int:comment_pk>/', views.comment_delete, name='comment_delete'),
]