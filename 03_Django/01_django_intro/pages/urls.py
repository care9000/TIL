from django.urls import path
from . import views

urlpatterns = [
    path('static_example/', views.static_example),
    path('user_create/', views.user_create),
    path('user_new/', views.user_new),
    path('result/', views.result),
    path('art/', views.art),
    path('pong/',views.pong),
    path('ping/',views.ping),
    path('catch/', views.catch),
    path('throw/', views.throw),
    path('isbirth/', views.isbirth),
    path('template_language/', views.template_language),
    path('dinner/', views.dinner),
    path('index/', views.index),   
    path('introduce/', views.introduce),
    path('images/', views.images),
    path('hello/<str:name>/<int:age>/', views.hello),
    path('hi/<str:name>/<int:age>/', views.hi),
    path('mul/<int:n1>/<int:n2>/', views.mul),
    path('circle/<int:r>', views.circle),
    path('pal/<name>/', views.pal),
    path('lotto/', views.lotto),
]
