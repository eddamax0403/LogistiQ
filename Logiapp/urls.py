
from django.contrib import admin
from django.urls import path
from Logiapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('pricing/',views.pricing,name='pricing'),
    path('services/',views.services,name='services'),
    path('servicedetails/',views.servicedetails,name='servicedetails'),
    path('starter/',views.starter,name='starter'),
    path('getquote/',views.getquote,name='getquote'),
    path('login/',views.login_view,name='login'),
    path('',views.register,name='register'),

    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
    path('transactions/', views.transactions_list, name='transactions'),

]
