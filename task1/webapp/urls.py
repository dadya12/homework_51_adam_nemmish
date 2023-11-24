from django.urls import path
from webapp.views import main, views, choose

urlpatterns = [
    path('', main, name='main'),
    path('cat_stats/', views, name='stats'),
    path('choose/', choose, name='choose'),
]