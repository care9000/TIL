from django.urls import path
from . import views


urlpatterns = [
    path('', views.index), #인덱스 페이지
    path('mamago/', views.mamago),
    path('translated/', views.translated),
]