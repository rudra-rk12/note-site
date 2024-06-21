from django.contrib import admin
from django.urls import path
from firstapp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('pricing', views.pricing, name='pricing'),
    path('features', views.features, name='features'),
    path('contact', views.contact, name='contact')

]