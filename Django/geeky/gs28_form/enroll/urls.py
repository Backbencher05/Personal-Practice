from django.urls import path
from django.urls.resolvers import URLPattern
from enroll import views
from django.urls import path

urlpatterns = [
    path('regis/', views.showformdata),
]