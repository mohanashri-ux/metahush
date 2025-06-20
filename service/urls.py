from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views
urlpatterns = [
   
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login_view,name='login'),
    path('logout',views.logout,name='logout'),
    path('dog-breeds',views.dog_breed_list,name='dog-breeds'),
    # path('dog-breed/<slug:slug>/', views.detail, name='detail'),
    path('cat-breeds',views.cat_breed_list,name='cat-breeds'),
    path('fish-breeds', views.fish_breed_list, name='fish-breeds'),
    path('other-breeds', views.other_breed_list, name='other-breeds'),
    path('bird-breeds', views.bird_breed_list, name='bird-breeds'),
    path('<str:species>-breed/<slug:slug>/', views.detail, name='detail'),
    path('appointment/', views.appointment_form, name='appointment_form'),
    path('submit-appointment/', views.submit_appointment, name='submit_appointment'),
    path('confirm-appointment/', views.confirm_appointment, name='confirm_appointment'),
    path('', views.index, name='index'),  # assuming you have a home view





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)