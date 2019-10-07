from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('articles/', include('articles.urls')),#articles/로 보내준다.
    path('admin/', admin.site.urls),
]
