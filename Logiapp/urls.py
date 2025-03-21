
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
    path('bookings/',views.bookings,name='bookings'),
    path('admindashboard/',views.admin_dashboard,name='admin'),
    path('adminlogin/',views.admin_login,name='adminlogin'),


    path('login/',views.login_view,name='login'),
    path('logout/',views.user_logout, name='logout'),
    path('book/',views.book,name='book'),
    path('',views.register,name='register'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit, name='edit'),

    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
    path('transactions/', views.transactions_list, name='transactions'),

]
