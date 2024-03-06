from django.urls import path

from . import views

urlpatterns = [
    path('callBack', views.CallBackRequest.as_view(), name='callBack'),
]