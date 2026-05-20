from django.contrib.auth import views as auth_views
from django.urls import path,include
from.import views


urlpatterns = [
    path('',views.index, name='index'),
    path('about',views.about, name='about'),
    path('booking',views.bookings, name='booking'),
    path('doctors',views.doctors, name='doctors'),
    path('departments',views.department, name='departments'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('signup',views.signup, name='signup'),
    
    
]
