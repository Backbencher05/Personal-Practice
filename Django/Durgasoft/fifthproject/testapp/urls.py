#from django.contrib import admin
from django.urls import path
from django.urls.resolvers import URLPattern
from testapp import views
urlpatterns = [
    path('first/', views.first_views),
    path('second/', views.second_views),
    path('third/', views.third_views),
    path('fourth', views.fourth_views),
    path('fifth/', views.fifth_views),
]
