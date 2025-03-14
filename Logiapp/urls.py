
from django.contrib import admin
from django.urls import path
from Logiapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('pricing/',views.pricing,name='pricing'),
    path('services/',views.services,name='services'),
    path('servicedetails/',views.servicedetails,name='servicedetails'),
    path('starter/',views.servicedetails,name='servicedetails'),
    path('getquote/',views.getquote,name='getquote'),


]
