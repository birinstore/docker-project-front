from django.urls import path
from . import views

urlpatterns = [
    path('', views.GalleryPage.as_view(), name='gallery'),
]
