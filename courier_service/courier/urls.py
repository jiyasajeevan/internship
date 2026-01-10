from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add_parcel/', views.add_parcel, name='add_parcel'),
    path('my_parcels/', views.my_parcels, name='my_parcels'),
    path('parcel/<int:parcel_id>/tracking/', views.parcel_tracking, name='parcel_tracking'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('update_parcel/<int:parcel_id>/', views.update_parcel_status, name='update_parcel_status'),
]