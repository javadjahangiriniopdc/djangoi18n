from django.contrib import admin
from django.urls import path, include

from testi18n import views

urlpatterns = [
    # path('', views.IndexPage.as_view(), name='index'),

    path('test/', views.TestView.as_view(), name='TestView'),

]
