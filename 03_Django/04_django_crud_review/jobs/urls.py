from django.urls import path
from .models import Job
from . import views

app_name = 'jobs'

urlpatterns = [
    path('past_life/',views.past_life, name='past_life'),
    path('',views.index, name='index'),

]