from django.urls import path
from . import views


from django.urls import path

urlpatterns = [

    path('', views.HomePageView.as_view(), name='home'),
]
