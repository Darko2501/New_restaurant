from django.urls import path
from .models import Menu
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('login_user/', views.login_user , name='login'),
    path('logout_user/', views.logout_user, name='logout'),
    path('register_user/', views.register_user, name='register'),
    path('book/',views.book,name='book'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)