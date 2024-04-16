from django.urls import path
from .import views
app_name = 'ads'
urlpatterns = [
     path('', views.index, name='index'),
     path('ad/', views.ads, name='ad'),
     path('ad/<int:ad_id>/', views.ad, name='ads'),
]