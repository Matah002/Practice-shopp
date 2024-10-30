from  django.contrib.auth import views as auth_views

from django.urls import path

from . import views

app_name = 'foodie'

urlpatterns = [
    path('become_vendor/', views.become_vendor, name='become_vendor'),
    path('vendor_page/', views.vendor_page, name='vendor_page'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='vendor/login.html'), name='login'),
]





